"""Latest Possible Start Time
Backward scheduler
倒排"""

import logging
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


class LPSTScheduler(object):
    def __init__(self, jobs, routes, **kwargs):
        self.jobs = jobs
        self.routes = routes

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run(self, job_list):
        for i, job in enumerate(job_list):
            self.schedule_job(job)

    def calculate_lpst(self, operation):
        # Calculate the latest possible start time for an operation
        lpst = operation.due_date - operation.processing_time
        for successor in operation.successors:
            lpst = min(lpst, successor.lpst - successor.processing_time)
        return lpst

    def schedule_job(self, job):
        # Schedule the operations of a job based on LPST
        operations_sequence = job.route.operations_sequence[::-1]
        latest_end_time = job.demand_date
        print(latest_end_time)

        for operation in operations_sequence:
            operation.lpst = self.calculate_lpst(operation)
            operation.start_time = operation.lpst
            operation.end_time = operation.lpst + operation.processing_time

    def rescheduling_job(self, job):
        return
