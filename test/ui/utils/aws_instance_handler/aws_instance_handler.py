"""
Handling AWS instances (especially Selenium Grid Machine) like- starting, stopping, getting instance
information etc.
"""
import datetime
import time

import boto3
import pytest
import requests


class AWSInstanceHandler:
    """
    This class contains methods for controlling AWS EC2 instances i.e.- starting, stopping, checking status
    etc.
    """

    def __init__(self, region='us-east-1', instances=('i-0b8b669f9c12dc34b',)):
        """
        Initialize an object for AWSInstanceHandler with attributes like - region of the EC2 instances,
        list of instances etc

        :param region: in which region your expected EC2 instances are located i.e:- 'us-east-1', 'us-west-2'
        etc
        :param instances list of instances on which actions to be performed or statuses to be checked.
        """
        self.region = region
        self.instances = instances
        self.ec2 = boto3.client('ec2', region_name=self.region,
                                aws_access_key_id=pytest.configs.get_config('aws_access_key_id'),
                                aws_secret_access_key=pytest.configs.get_config('aws_secret_access_key'),
                                )

    def start_instances(self, instance_ids=None):
        """
        Starts a list of instances specified by their instance ids.

        :param instance_ids EC2 instance id list which are to be started.
        """
        _instance_ids = self.instances if instance_ids is None else instance_ids
        self.ec2.start_instances(InstanceIds=_instance_ids)
        print('\nStarted instances: ' + str(_instance_ids))

    def stop_instances(self, instance_ids=None):
        """
        Stops a list of instances specified by their instance ids.

        :param instance_ids EC2 instance id list which are to be stopped.
        """
        _instance_ids = self.instances if instance_ids is None else instance_ids
        self.ec2.stop_instances(InstanceIds=_instance_ids)
        print('\nStopped instances: ' + str(_instance_ids))

    def get_instance_status(self, instance_id='i-0b8b669f9c12dc34b'):
        """
        Gets the status of a specified EC2 instance's status. Statuses- running, pending, stopped, terminated etc.

        :param instance_id EC2 instance id for which status is to be returned.
        """

        resource = boto3.resource('ec2', region_name=self.region,
                                  aws_access_key_id=pytest.configs.get_config('aws_access_key_id'),
                                  aws_secret_access_key=pytest.configs.get_config('aws_secret_access_key'),
                                  )
        instance_status = resource.Instance(instance_id).state['Name']
        return instance_status

    def is_instance_running(self, instance='i-0b8b669f9c12dc34b'):
        """
        Returns whether an EC2 instance is running.
        """
        return self.get_instance_status(instance) == 'running'

    def is_instance_stopped(self, instance='i-0b8b669f9c12dc34b'):
        """
        Returns whether an EC2 instance is stopped.
        """
        return self.get_instance_status(instance) == 'stopped'

    def is_instance_pending(self, instance='i-0b8b669f9c12dc34b'):
        """
        Returns whether an EC2 instance is pending.
        """
        return self.get_instance_status(instance) == 'pending'

    def wait_for_instance_until(self, status='running', instance_id='i-0b8b669f9c12dc34b', max_wait=300,
                                check_interval=2):
        """
        Waits for an instance's specified status.
        :param status expected status to be reached
        :param instance_id id of the expected EC2 instance
        :param max_wait maximum wait time until it return False. Default is 300 secs.
        :param check_interval interval by which status of the instance is to be checked
        """
        total_iteration = max_wait // check_interval

        for _ in range(total_iteration):
            time.sleep(check_interval)
            if self.get_instance_status(instance_id) == status:
                return True
        return False

    def is_selenium_grid_ready(self):
        grid_response = self.ec2.describe_instance_status(InstanceIds=self.instances)
        instance_status = grid_response['InstanceStatuses'][0]['InstanceStatus']['Status']
        system_status = grid_response['InstanceStatuses'][0]['SystemStatus']['Status']
        return instance_status == 'ok' and system_status == 'ok'

    @staticmethod
    def is_containers_ready_in_grid(wait_time=600, check_interval=10):
        selenium_grid_ui_url = pytest.configs.get_config('selenium_grid_ui')
        is_url_accessible = False
        start_time = datetime.datetime.now()

        while True:
            time.sleep(check_interval)
            try:
                selenium_grid_response = requests.get(selenium_grid_ui_url)
                is_url_accessible = True if selenium_grid_response.status_code == 200 else False
            except requests.exceptions.ConnectionError as connection_error:
                print(f'Error occurred: {connection_error.response}')

            if (datetime.datetime.now() - start_time).seconds >= wait_time:
                return False

            if is_url_accessible:
                time.sleep(60)
                return True

    # pylint: disable=broad-exception-caught
    def check_if_selenium_grid_ready(self, wait_time=900, check_interval=2):
        """
        Checks if System is ready to go. We assume that, if the system check passes then Selenium Grid
        might have started.
        :param wait_time maximum time until it returns False
        :param check_interval interval by which status of the instance is to be checked
        """
        total_iteration = wait_time // check_interval
        for _ in range(total_iteration):
            time.sleep(check_interval)
            try:
                is_selenium_grid_ready = self.is_selenium_grid_ready()
                if is_selenium_grid_ready:
                    return True
            except Exception as ce:
                if hasattr(ce, 'message'):
                    print(ce.message)
                else:
                    print(ce)
        return False
