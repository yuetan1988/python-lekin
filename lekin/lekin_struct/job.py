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

ob1 = Job(1, datetime(2023, 7, 25), 1, 1)
job2 = Job(2, datetime(2023, 7, 26), 2, 1)

operation1 = Operation(1, [1, 2], 2, 2, None)
operation2 = Operation(2, [3], 3, None, 1)

job_collector = JobCollector()
job_collector.add_job(job1)
job_collector.add_job(job2)
job_collector.add_operation(operation1)
job_collector.add_operation(operation2)

# Get operations for Job 1 and Route 1
job1_operations_route1 = job_collector.get_operations_by_job_and_route(1, 1)
print("Job 1 Operations (Route 1):")
for op in job1_operations_route1:
    print("Operation ID:", op.operation_id)
"""

from typing import Any, Callable, Dict, List, Optional, Tuple


class JobCollector:
    def __init__(self):
        self.jobs = []  # List to store Job objects
        self.operations = []
        self.routes = []
        self.resources = []
        self.time_slots = []

    def add_job(self, job):
        self.jobs.append(job)

    def add_operation(self, operation):
        self.operations.append(operation)

    def get_job_by_id(self, job_id):
        for job in self.jobs:
            if job.job_id == job_id:
                return job
        return None

    def get_operations_by_job_and_route(self, job_id, route_id):
        job_operations = []
        for operation in self.operations:
            if operation.parent_operation_id is None and operation.route_id == route_id:
                # If the operation is the first operation in the route
                current_operation = operation
                while current_operation:
                    if current_operation.job_id == job_id:
                        job_operations.append(current_operation)
                    next_operation_id = current_operation.next_operation_id
                    current_operation = next(
                        (op for op in self.operations if op.operation_id == next_operation_id), None
                    )
        return job_operations

    def get_schedule(self):
        schedule = {}

        for resource in self.resources:
            scheduled_operations = []
            for operation in self.operations:
                if operation.resource == resource:
                    scheduled_operations.append({"operation_id": operation.id, "start_time": operation.start_time})

            if scheduled_operations:
                schedule[resource.id] = scheduled_operations

        return schedule


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
