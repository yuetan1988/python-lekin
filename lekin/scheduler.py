"""Flexible job shop scheduler"""

from collections import OrderedDict
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple

from lekin.datasets.check_data import check_data


class Scheduler(object):
    def __init__(self, objective, solver):
        self.objective = objective
        self.solver = solver

    def solve(self, jobs, machines, max_operations):
        self.solver.solve(jobs, machines)

    def evaluate(self):
        pass

    def plot(self):
        pass
