"""
Struct Job
    - a job could finish one product while finished
    - job/mo/operation/activity

property
    - processing time
    - due date
    - weight
    - slack time remaining
    - critical ratio
    - priority
"""

from typing import List, Dict, Any, Callable, Optional, Tuple


class Job(object):
    def __init__(
            self,
            route_id,
            route_name,
            route_color,
            task_id,
            machine_id,
            machine_name,
            duration):
        self.route_id = route_id

    def __eq__(self, other):
        return

    def __hash__(self):
        return

    def __str__(self):
        return
