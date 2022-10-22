"""Shortest Processing Time"""


class SPT(object):
    def __init__(self):
        self.time = {}
        self.waiting_jobs = {}
        self.current_time_on_machines = {}
        self.export_jobs_list = []

    def setup(self, job_list, machine_list):
        for machine in machine_list:
            # init for machine start time
            self.current_time_on_machines[machine.name] = 0

            # init for waiting list of machines
            self.waiting_jobs[machine.name] = 0
            for job in job_list:
                if job.operation_id == 1 and machine.name in job.machine:
                    if len(job.machine) == 1:
                        self.waiting_jobs[machine.name].append(job)
        return

    def solve(self, job_list, machine_list):
        self.setup(job_list, machine_list)
