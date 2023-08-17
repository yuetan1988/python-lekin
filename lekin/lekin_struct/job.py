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

from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Tuple

from lekin.lekin_struct.operation import Operation


class Job(object):
    def __init__(
        self,
        job_id: str,
        priority: int = None,
        quantity: int = None,
        demand_date: datetime = None,
        job_type: str = None,
        earliest_start_time=None,
        assigned_route_id=None,
        assigned_bom_id=None,
        **kwargs,
    ):
        self.job_id = job_id
        self.priority = priority
        self.demand_date = demand_date
        self.quantity = quantity
        self.job_type = job_type
        self.earliest_start_time = earliest_start_time  # Material constraint
        self.assigned_route_id = assigned_route_id  # Route object assigned to this job
        self.assigned_bom_id = assigned_bom_id
        self.assigned_operations = []  # List of Operation objects assigned to this job

        for key, value in kwargs.items():
            setattr(self, key, value)

    def assign_route(self, route_id):
        self.assigned_route_id = route_id

    @property
    def operations(self):
        return self.assigned_operations

    def __eq__(self, other):
        return

    def __hash__(self):
        return

    def __str__(self):
        return f"{self.job_id}"


class JobCollector:
    def __init__(self):
        self.job_list = []  # List to store Job objects
        self.index = -1
        # self.route_list = []  # List to store route with sequence of jobs
        # self.operation_list = []
        # self.resource_list = []
        # self.time_slot_list = []

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.job_list):
            return self.job_list[self.index]
        else:
            raise StopIteration("Stop")

    def add_job(self, job: Job) -> None:
        self.job_list.append(job)

    def get_job_by_id(self, job_id: str):
        for job in self.job_list:
            if job.job_id == job_id:
                return job
        return None

    def get_schedule(self):
        schedule = {}

        for resource in self.resource_list:
            scheduled_operations = []
            for operation in self.operation_list:
                if operation.resource == resource:
                    scheduled_operations.append({"operation_id": operation.id, "start_time": operation.start_time})

            if scheduled_operations:
                schedule[resource.id] = scheduled_operations

        return schedule
