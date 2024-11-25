import os
import sys

from cryptography.fernet import Fernet

source_file = input('Enter source file: ') or 'env_var_pairing.csv'
destination_file = input('Enter destination file: ') or 'axgo_profile'
variable_prefix = input('Enter ENV_VAR prefix: ') or 'AXGO_'
secret_key = input('Enter your secret key: ') or 'tdFTJJ0L55pJwb-PF2if6ztiwcooeXESJEoW_Izg46I='

parent_directory = os.path.dirname(__file__)

with open(f'{parent_directory}/{source_file}', 'r') as env_file:
    destination_file_descriptor = open(f'{parent_directory}/{destination_file}', 'w')
    cipher = Fernet(secret_key)
    sys.stdout = destination_file_descriptor
    for line, text in enumerate(env_file):
        if line != 0:
            ENV_VAR_NAME, ENV_VAR_VALUE = text.split(',')
            _ENV_VAR_NAME = f'{variable_prefix}{ENV_VAR_NAME}'
            _ENV_VAR_VALUE = cipher.encrypt(str.encode(ENV_VAR_VALUE))

            print(f"export {_ENV_VAR_NAME}='{_ENV_VAR_VALUE.decode()}'")
    
    
    destination_file_descriptor.close()