<<<<<<< HEAD
"""Flexible job shop scheduler"""

from collections import OrderedDict
import logging
from typing import Any, Callable, Dict, List, Optional, Tuple

from lekin.datasets.check_data import check_data


=======
>>>>>>> bba1022 (update readme)
class Scheduler(object):
    def __init__(self, objective, solver):
        self.objective = objective
        self.solver = solver

    def solve(self, jobs, machines, max_operations):
        self.solver.solve(jobs, machines)

    def evaluate(self):
        pass

    def draw(self):
        pass
