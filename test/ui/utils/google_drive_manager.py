import datetime
import os.path
import shutil
from os.path import join

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import ApiRequestError

from utils.app_constants import AppConstant


class GoogleDriveManager:
    def __init__(self, client_config_file=AppConstant.CLIENT_CONFIG_FILE):
        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_config_file
        gauth = GoogleAuth()

        gauth.LoadCredentialsFile(AppConstant.GOOGLE_CREDENTIAL_FILE)
        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile(AppConstant.GOOGLE_CREDENTIAL_FILE)

        self.drive = GoogleDrive(gauth)

    def get_list_of_files_by_id(self, folder_id=None):
        files = self.drive.ListFile({'q': f"'{folder_id}' in parents", 'orderBy': 'modifiedDate desc'}).GetList()
        return {file['title'].lower(): file['id'] for file in files}

    def get_list_of_filtered_files_by_id(self, folder_id=None, file_type=None):
        files = self.drive.ListFile({'q': f"'{folder_id}' in parents", 'orderBy': 'modifiedDate desc'}).GetList()
        if file_type:
            return {file['title'].lower(): file['id'] for file in files if file['title'].endswith(file_type)}
        else:
            return {file['title'].lower(): file['id'] for file in files}

    def get_list_of_files_by_name(self, folder_name):
        folder_id = self.get_folder_id(folder_name)
        return self.get_list_of_files_by_id(folder_id)

    def get_file_info_by_id(self, file_id, info_key=None):
        files_info = self.drive.ListFile({'q': f"'{file_id}' in parents"}).GetList()
        if not files_info:
            print('File not found in the Google Drive folder.')
            return None
        if info_key:
            return files_info[0][info_key]
        return files_info[0]

    def get_folder_id(self, folder_name):
        all_folders = self.drive.ListFile(
            {"q": "mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        return [folder['id'] for folder in all_folders if folder_name == folder['title']][0]

    def get_latest_file_id_by_extension(self, folder_id, extension):
        """
        This method returns the ID of the latest file in a Google Drive folder
        with the specified extension.
        """
        # Get the list of files in the folder
        files = self.get_list_of_files_by_id(folder_id)
        # Filter the files to only include those with the specified extension
        matching_files = [file for file in files if
                          isinstance(file, dict) and file.get('mimeType') == 'application/zip' and file.get('title',
                                                                                                            '').endswith(
                              extension)]
        if not matching_files:
            print(
                f"No files with the extension '{extension}' found in folder with ID '{folder_id}'. Files in folder: {files}")
            raise FileNotFoundError()

        sorted_files = sorted(matching_files, key=lambda f: f['modifiedDate'], reverse=True)
        if not sorted_files:
            raise FileNotFoundError()
        return sorted_files[0]['id']

    def download_file(self, file_id, destination_file_name, destination_folder_name=AppConstant.APK_FOLDER):
        file = self.drive.CreateFile({'id': file_id})
        print(f'\nDownloading file {file_id} in directory {destination_folder_name} as {destination_file_name} ...\n')
        if not os.path.exists(destination_folder_name):
            os.makedirs(destination_folder_name)
        file.GetContentFile(join(destination_folder_name, destination_file_name))
        print('File downloaded successfully.')

    def download_file_by_id(self, file_id, file_path):
        try:
            file = self.drive.CreateFile({'id': file_id})
            print(f'\nDownloading file {file_id} in directory {file_path}  ...\n')
            file.GetContentFile(file_path)
            return True
        except ApiRequestError as e:
            print('An error occurred: %s' % e)
            return False

    # def get_latest_zip_file_id(self, parent_folder_id):
    #     query = f"'{parent_folder_id}' in parents and trashed = false and mimeType = 'application/zip'"
    #     # query = f"'{parent_folder_id}' in parents and trashed = false"
    #     file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()
    #     if len(file_list) > 0:
    #         return file_list[0]['id']
    #     else:
    #         raise Exception('No .zip file found in the parent folder.')

    
    # def get_latest_zip_file_id(self,version_folder_id,env):
    #     query = (
    #         f"'{version_folder_id}' in parents and trashed = false and "
    #         f"mimeType = 'application/zip' and title contains '{env}'"
    #     )
    #     file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()
    #     if len(file_list) > 0:
    #         return file_list[0]['id']
    #     else:
    #         raise Exception(f"No .zip file found in the current folder containing {env} in its name.")

    
    def get_latest_zip_file_id(self, version_folder_id, env:str):
        # Convert the search string to lowercase for case-insensitive comparison
        env_lower = env.lower()
        
        # Query to get all files within the specified folder
        query = (
            f"'{version_folder_id}' in parents and trashed = false and "
            f"mimeType = 'application/zip'"
        )
        file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()

        # Filter files containing the partial match substring (case-insensitive)
        filtered_files = [file for file in file_list if env_lower in file['title'].lower()]

        if len(filtered_files) > 0:
            return filtered_files[0]['id']
        else:
            raise Exception(f"No .zip file found in the current folder containing '{env}' in its name.")

    # def get_latest_zip_file_modified_date(self, parent_folder_id):
    #     query = f"'{parent_folder_id}' in parents and trashed = false and mimeType = 'application/zip'"
    #     file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()
    #     if len(file_list) > 0:
    #         return file_list[0]['modifiedDate']
    #     else:
    #         raise Exception('No .zip file found in the parent folder.')


    # def get_latest_zip_file_modified_date(self, version_folder_id, env):
    #     query = (
    #         f"'{version_folder_id}' in parents and trashed = false and "
    #         f"mimeType = 'application/zip' and title contains '{env}'"
    #     )
    #     file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()
    #     if len(file_list) > 0:
    #         return file_list[0]['modifiedDate']
    #     else:
    #         raise Exception('No .zip file found in the parent folder.')

        
    def get_latest_zip_file_modified_date(self, version_folder_id, env:str):
        # Convert the search term to lowercase for case-insensitive comparison
        env_lower = env.lower()
        
        # Query to get all files within the specified folder
        query = (
            f"'{version_folder_id}' in parents and trashed = false and "
            f"mimeType = 'application/zip'"
        )

        
        # Retrieve the file list from the drive
        file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()

        # Filter files containing the partial match substring (case-insensitive)
        filtered_files = [file for file in file_list if env_lower in file['title'].lower()]

        if len(filtered_files) > 0:
            # Return the modifiedDate of the latest file
            return filtered_files[0]['modifiedDate']
        else:
            raise Exception('No .zip file found in the parent folder.')

    def get_latest_zip_file_name(self, parent_folder_id):
        query = f"'{parent_folder_id}' in parents and trashed = false and mimeType = 'application/zip'"
        file_list = self.drive.ListFile({'q': query, 'orderBy': 'modifiedDate desc'}).GetList()
        latest_file = file_list[0]
        file_name = os.path.splitext(latest_file['title'])[0]
        return file_name

    def get_the_latest_ipa_file_name_from_apk_folder(self, apk_folder_path):
        for filename in os.listdir(apk_folder_path):
            if filename.endswith(".ipa"):
                return filename
        raise ValueError(f"No .ipa file found in folder {apk_folder_path}")

    def download_and_extract_zip_file(self, file_id, destination_folder_name):
        file = self.drive.CreateFile({'id': file_id})
        print(f'\nDownloading file {file_id} in directory {destination_folder_name} ...\n')
        file.GetContentFile('latest.zip')
        shutil.unpack_archive('latest.zip', destination_folder_name)
        print('File downloaded and extracted successfully.')

    def find_env_folder(self, extracted_path, environment):
        """Find the folder for the specified environment within the extracted folder."""
        env_folder = os.path.join(extracted_path, f'{environment}')
        return env_folder

    # def download_ipa_file(self, env_folder, destination_folder):
    #     """Find and download the .ipa file from the specified environment folder."""
    #     # ipa_file = None
    #     # Find the .ipa file in the subfolder
    #     for file_name in os.listdir(env_folder):
    #         if file_name.endswith(".ipa"):
    #             ipa_file_path = os.path.join(env_folder, file_name)
    #             break
    #     else:
    #         raise ValueError(f"No .ipa file found in {env_folder}")
    #     shutil.copy(ipa_file_path, destination_folder)

    def download_ipa_file(self, env_folder, destination_folder, destination_file_name):
        """Find and download the .ipa file from the specified environment folder and its subfolders."""
        ipa_file_path = None

        # Walk through all directories and subdirectories in env_folder
        for root, _, files in os.walk(env_folder):
            for file_name in files:
                if file_name.endswith(".ipa"):
                    ipa_file_path = os.path.join(root, file_name)
                    break
            if ipa_file_path:
                break
        else:
            raise ValueError(f"No .ipa file found in {env_folder} and its subfolders")

        new_file_path = os.path.join(env_folder, destination_file_name)
        # Rename the file
        os.rename(ipa_file_path, new_file_path)
        # Copy the .ipa file to the destination folder
        shutil.copy(new_file_path, destination_folder)
        print(f"Copied {new_file_path} to {destination_folder}")

    def get_the_latest_ipa_file_env_folder_name(self):
        date_format = '%Y-%m-%dT%H:%M:%S.%f%z'
        destination_folder = f'{AppConstant.APK_FOLDER}'
        extracted_folder_path = os.path.join(destination_folder, 'extracted')
        parent_folder_id = self.get_folder_id('Lynx IPA & Apps')
        file_id = self.get_latest_zip_file_id(parent_folder_id)
        apk_modified_date_time_str_in_gd = self.get_latest_zip_file_modified_date(parent_folder_id)
        apk_modified_date_time_in_gd = datetime.datetime.strptime(apk_modified_date_time_str_in_gd, date_format)
        apk_modified_date_time_in_gd = apk_modified_date_time_in_gd.replace(tzinfo=datetime.timezone.utc)
        # Get the current datetime object with timezone information
        current_date_time = datetime.datetime.now(datetime.timezone.utc)

        if apk_modified_date_time_in_gd > current_date_time:
            os.makedirs(destination_folder, exist_ok=True)
            os.makedirs(extracted_folder_path, exist_ok=True)
            self.download_and_extract_zip_file(file_id, extracted_folder_path)
            # Get the first folder name in the extracted directory
            first_folder_name = os.listdir(extracted_folder_path)[0]
            extracted_file_path = f'{extracted_folder_path}/{first_folder_name}'
            for item in os.listdir(extracted_file_path):
                item_path = os.path.join(extracted_file_path, item)
                if os.path.isdir(item_path):
                    return os.path.basename(item_path)
        else:
            print('\nGoogle drive has no latest apk. Ending the current session...\n')
        shutil.rmtree(extracted_folder_path, ignore_errors=True)