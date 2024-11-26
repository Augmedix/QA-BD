import pytest
import requests
from test.ui.utils import helper
from test.ui.utils.app_constants import AppConstant

def read_file(path: str):
    """
    Opens a file and reads its content.
    """
    with open(path, 'rb') as file:
        return file.read()

class LambdaManager:
    """
    Contains a couple of methods to help managing apks.
    """
    def __init__(self, lambdatest_username=None, lambdatest_access_key=None):
        """
        Initialize manager to prepare necessary data used by corresponding methods.
        """
        self.lambdatest_username = lambdatest_username or pytest.configs.get_config('lambdatest_username')
        self.lambdatest_access_key = lambdatest_access_key or pytest.configs.get_config('lambdatest_access_key')
        self.lambdatest_base_url = 'https://manual-api.lambdatest.com/app/'
        self.upload_path = 'upload/realDevice'
        self.app_data_path = 'data'
        self.auth = (self.lambdatest_username, self.lambdatest_access_key)
        self.custom_id_length = 8
        self.success_status_code = 200
        self.image_type = 'image'

    def get_app_id_after_uploading_apk(self, app_name='GO_Automation', apk_file_path=None):
        """
        Used to upload & get the APP_ID for the uploaded apk file to lambdatest.
        :param app_name - expected name to be displayed in lambdatest.
        :param apk_file_path - the location for the apk to upload.
        """
        files = {
            'appFile': open(apk_file_path, 'rb'),
            'name': (None, app_name),
        }
        print('\nUploading apk file to LambdaTest...\n')
        _response = requests.post(f'{self.lambdatest_base_url}{self.upload_path}', files=files, auth=self.auth)
        print('\nUploading apk file to LambdaTest is completed.\n')
        return _response.json()['app_id']

    def get_apk_infos(self):
        """
        Get all the apk info for a specific user.
        """
        params = {
            'type': 'ios',
            'level': 'user',
        }
        response = requests.get(
            f'{self.lambdatest_base_url}{self.app_data_path}',
            params=params,
            auth=self.auth,
        )
        return response.json()['data']

    def get_apk_info(self, apk_name='', info_key='app_id'):
        """
        Get app_id with a specific name.
        """
        apk_info_list = self.get_apk_infos()
        for apk_info in apk_info_list:
            if apk_info['name'] == apk_name:
                return apk_info[info_key]
            
    def check_app_id_exist(self, app_id=None):
        apk_infos = self.get_apk_infos()
        for apk_info in apk_infos:
            if app_id.endswith(apk_info['app_id']):
                return True
        return False
    
    def upload_file(self, upload_url: str, username: str, access_key: str, screenshot_data: bytes, params: dict):
        """
        Makes the API request to upload the screenshot.
        """
        response = requests.post(upload_url, auth=(username, access_key), files={'media_file': screenshot_data},
                                 data=params, timeout=900)
        if response.status_code == self.success_status_code:
            media_url = response.json()['media_url']
            print('QR IMAGE uploaded successfully:', media_url)
        else:
            print('QR IMAGE upload screenshot:', response.text)
        return response

    def start_qr_upload(self):
        # Set your LambdaTest username and access key
        username = self.lambdatest_username
        access_key = self.lambdatest_access_key

        # Set the API endpoint to upload the screenshot
        upload_url = pytest.configs.get_config('lamdatest_qr_upload_url')
        custom_id = helper.generate_custom_id(self.custom_id_length)

        # Set the parameters for the API request
        params = {
            'type': self.image_type,
            'custom_id': custom_id,
        }
        # Open the screenshot file and read its content
        screenshot_data = read_file(self.picture_path)

        # Make the API request to upload the screenshot
        response = self.upload_file(upload_url, username, access_key, screenshot_data, params)
        return (
            response.json().get('media_url')
            if response.status_code == self.success_status_code
            else None
        )