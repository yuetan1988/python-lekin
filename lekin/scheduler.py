"""Flexible job shop scheduler"""

import logging

from lekin.datasets.check_data import check_data


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
