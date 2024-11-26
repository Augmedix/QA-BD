import requests
import jwt
import pytest
from jwt import DecodeError
import json
import random
import uuid
from test.ui.pages.api_pages.base_page import BasePage
from test.ui.utils.api_request_data_handler import APIRequestDataHandler
from test.ui.utils.helper import get_formatted_date_str
from test.ui.utils.request_handler import RequestHandler
from test.ui.pages.api_pages.appointment_api_page import AppointmentsApiPage
from test.ui.utils.upload_go_audio.upload_audio import upload_audio_to_go_note
import time


class TranscriptApiPage(BasePage):
    def __init__(self):
        self.appointment_page = AppointmentsApiPage()
    #     super().__init__(db)

    auth_base_url = pytest.configs.get_config('authorization_base_url')
    transcript_base_url = pytest.configs.get_config('transcript_base_url')

    def get_transcript_api_response(self, stream_id, request_path='', headers=None, token=None, max_wait=120):
        start_time = time.time()
        while True:
            response = RequestHandler.get_api_response(base_url=self.transcript_base_url, request_path=request_path, headers=headers, token=token)
            if response.json() != [] and response.json()[-1]['id'] == stream_id:
                break
            if time.time() - start_time > max_wait:
                print("Max time limit reached. Audio uploading took too long")
                break
            time.sleep(1)
        return response


    def upload_an_audio_file_and_get_transcription(self, token, headers, note_id, file_path, email, password, max_wait=120):
        # Upload an audio to note
        stream_id, generated_token = upload_audio_to_go_note(auth_token=token, note_id=note_id, file_path=file_path, username=email,password=password)
        request_path = f'{note_id}/{stream_id}'
        start_time = time.time()
        while True:
            response = RequestHandler.get_api_response(base_url=self.transcript_base_url, request_path=request_path, headers=headers, token=generated_token)
            if response.status_code == 200:
                break
            if time.time() - start_time > max_wait:
                print("Max time limit reached. Transcription took too long")
                break
            time.sleep(1)
        return stream_id, response

        
        
            