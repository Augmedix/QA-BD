import json
import os

from test.ui.utils.app_constants import AppConstant


class JsonDataHandler:
    """
    This class is mainly responsible for loading json data from saved json files. To get the data
    loaded user must initialize the class with the expected json data file's name (excluding extension).
    All the json data files assume to be in the "json_data" folder under "resources" folder.
    """

    def __init__(self, datatype='') -> None:
        with open(os.path.join(AppConstant.JSON_DATA_FOLDER, f'{datatype}.json'), 'r', encoding='UTF-8') as json_file:
            json_data = json.loads(json_file.read())

        self.json_data = json_data
        self.datatype = datatype

    def get_key_value(self, name=''):
        """
        Returns the payload as json object.

        Returns:
            json_object: which represents the payload for the request to be sent.
        """
        return self.json_data[name]

