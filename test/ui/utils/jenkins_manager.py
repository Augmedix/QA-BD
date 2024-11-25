import datetime
from datetime import datetime

import jenkins


class JenkinsManager:
    def __init__(self):
        self.server = jenkins.Jenkins('https://qa-automation-bd.augmedix.com', username='sazib', password='@ugmed1X!')

    def get_all_jobs_name(self):
        jobs_info = self.server.get_all_jobs()
        return [job['name'] for job in jobs_info]

    def get_last_build_number_of(self, job_name=None):
        try:
            return self.server.get_job_info(job_name)['builds'][0]['number']
        except IndexError:
            return 0

    def get_last_build_execution_time_of(self, job_name, _build_number):
        try:
            return self.server.get_build_info(job_name, _build_number)['timestamp']
        except jenkins.JenkinsException:
            return 0

    def get_latest_build_time_of_jobs(self):
        jobs_list = self.get_all_jobs_name()
        build_numbers = [self.get_last_build_number_of(job) for job in jobs_list]
        latest_job_execution_time_list = [self.get_last_build_execution_time_of(job, build_number)
                                          for job, build_number in zip(jobs_list, build_numbers)]
        last_executed_job_time = max(latest_job_execution_time_list)
        return datetime.fromtimestamp(last_executed_job_time/1000)

    def is_running_job_present(self):
        jobs_info = self.server.get_all_jobs()
        return any([True for job in jobs_info if job['color'].endswith('_anime')])

    def get_running_jobs_count(self):
        jobs_info = self.server.get_all_jobs()
        return sum([1 for job in jobs_info if job['color'].endswith('_anime')])
