import datetime
import json

import pytest
import pytz
import requests

from test.ui.utils.uploadscript import nrt_upload


class S2THandler:
    api_base_url = pytest.configs.get_config('api_base_url')
    auth_url = pytest.configs.get_config('auth_url')
    recording_url = pytest.configs.get_config('recording_url')
    provider_email = pytest.configs.get_config('s2t_provider')
    scribe_email = pytest.configs.get_config('s2t_scribe')
    password = pytest.configs.get_config('password')
    provider_id = pytest.configs.get_config('s2t_provider_id')

    @staticmethod
    def get_auth_token(username, password):
        url = f'{S2THandler.api_base_url}/{S2THandler.auth_url}'

        payload = json.dumps({
            'username': username,
            'password': password,
            'otp': '',
            'userType': 'scribe'
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)

        return response.json()['token']

    @staticmethod
    def upload_audio_for_note():
        '''
        Uploads a recording file for live speech to text conversion.
        :param None
        :return None
        '''
        with open('resources/recordings/s2t.rec') as _recording_file:
            recording_file_content = str(_recording_file.read())

        url = f'{S2THandler.api_base_url}/{S2THandler.recording_url}'

        payload = json.dumps({
            'recordingFile': recording_file_content,
            'recordingId': f'dictation_22027_{id(5)}',
            'providerEmail': S2THandler.provider_email,
            'providerId': int(S2THandler.provider_id),
            'type': 'dictation',
            'patientName': f'new patient {id(5)}',
            'recordingStartTime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

        token = S2THandler.get_auth_token(S2THandler.scribe_email, S2THandler.password)

        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        requests.request('POST', url, headers=headers, data=payload)
        print('Recording file uploaded successfully...')

    def upload_nrt_recording(self, visit_type, doctor_email):
        upload_status = nrt_upload.nrt_api(pytest.configs.get_config('mcu_server'),
                                           visit_type,
                                           pytest.configs.get_config('recording_type'),
                                           pytest.configs.get_config('recording_file_path'),
                                           doctor_email,
                                           pytest.configs.get_config('doctor_pass'),
                                           pytest.configs.get_config('auth_url_nrt'),
                                           pytest.configs.get_config('note_creation_url'),
                                           pytest.configs.get_config('note_name'))

        return upload_status

    def upload_nrt_recording_on_same_note(self,response_list , visit_type):
        pst = pytz.timezone('America/Los_Angeles')
        date = datetime.datetime.now(pst)

        date.strftime('%H:%M')
        time = date.strftime('%I:%M %p').lower()
        print('date and time:', time)

        print(str(response_list[0]))
        print(str(response_list[1]))
        print(str(response_list[2]))

        stream_id = nrt_upload.upload_nrt_file(pytest.configs.get_config('mcu_server'), str(response_list[1]), str(response_list[2]),
                                   visit_type, pytest.configs.get_config('recording_type'),
                                   pytest.configs.get_config('recording_file_path2'), response_list[0])
        return stream_id[1] , time
