"""Earliest Possible Start Time
Forward scheduler
正排"""

import logging

from lekin.solver.construction_heuristics.base import BaseScheduler


class EPSTScheduler:
    def __init__(self, jobs, routes):
        self.jobs = jobs
        self.routes = routes

    def calculate_earliest_start_time(self, operation):
        # Calculate the earliest start time for an operation based on its dependencies
        if not operation.predecessors:
            return max(operation.available_time, 0)
        else:
            return max(op.end_time for op in operation.predecessors)

    def schedule_job(self, job):
        # Schedule the operations of a job using EPST method
        for operation in job.route.operations:
            operation.start_time = self.calculate_earliest_start_time(operation)
            operation.end_time = operation.start_time + operation.processing_time

    def run(self):
        for job in self.jobs:
            self.schedule_job(job)
