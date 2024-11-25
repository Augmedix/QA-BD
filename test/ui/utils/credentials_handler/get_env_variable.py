import os
import sys

from cryptography.fernet import Fernet

source_file = input('Enter source file: ') or 'axgo_profile'
secret_key = input('Enter your secret key: ') or 'tdFTJJ0L55pJwb-PF2if6ztiwcooeXESJEoW_Izg46I='

parent_directory = os.path.dirname(__file__)

with open(f'{parent_directory}/{source_file}', 'r') as env_file:
    cipher = Fernet(str.encode(secret_key))
    for line, text in enumerate(env_file.read().splitlines()):
            ENV_VAR_NAME, ENV_VAR_VALUE = text.split('=', maxsplit=1)
            print(f'{ENV_VAR_NAME.replace("export", "")}={cipher.decrypt(str.encode(ENV_VAR_VALUE)).decode()}')
