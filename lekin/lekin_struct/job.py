"""
Struct Job/订单作业
    - a job could finish one product while finished
    - job/mo/operation/activity

property
    - 已完成活动
    - 待完成活动
    - processing time
    - due date
    - weight
    - slack time remaining
    - critical ratio
    - priority
    - 属于哪个订单

method

"""

from typing import Any, Callable, Dict, List, Optional, Tuple


class JobCollector:
    def __init__(self):
        self.jobs = []  # List to store Job objects

    def add_job(self, job):
        self.jobs.append(job)

    def get_job_by_id(self, job_id):
        for job in self.jobs:
            if job.job_id == job_id:
                return job
        return None


class Job(object):
    def __init__(self, job_id, priority, demand_time, assigned_route, assigned_tree):
        self.job_id = job_id
        self.priority = priority
        self.demand_time = demand_time
        self.assigned_route = None  # Route object assigned to this job
        self.assigned_operations = []  # List of Operation objects assigned to this job

    def assign_route(self, route):
        self.assigned_route = route

    def assign_operation(self, operation):
        self.assigned_operations.append(operation)

    def __eq__(self, other):
        return

    def __hash__(self):
        return

    def __str__(self):
        return
