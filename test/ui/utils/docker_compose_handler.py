import pytest
import yaml
from utils.app_constants import AppConstant

class DockerComposeHandler:
    def __init__(self):
        with open(AppConstant.DOCKER_COMPOSE_TEMPLATE_FILE) as docker_compose_yaml:
            contents = yaml.safe_load(docker_compose_yaml)
        self.docker_compose_contents = contents

    def set_chrome_version(self):
        chrome_version = pytest.browser_version  # Accessing directly from pytest
        node_chrome_version = float(chrome_version.split('.')[0]) \
            if '.' in chrome_version else float(chrome_version)
        self.docker_compose_contents['services']['chrome']['image'] = f'selenium/node-chrome:{node_chrome_version}'

    def update_docker_compose_file(self):
        self.set_chrome_version()
        with open(AppConstant.DOCKER_COMPOSE_FILE, 'w') as docker_compose_yaml:
            yaml.dump(self.docker_compose_contents, docker_compose_yaml)
