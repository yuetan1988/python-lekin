"""Flexible job shop scheduler"""

import logging

from lekin.datasets.check_data import check_data


class Scheduler(object):
    def __init__(self, solver):
        self.solver = solver

    def run(self, jobs, machines, max_operation):
        self.solve(jobs, machines, max_operation)
        self.evaluate()
        self.draw()

    def solve(self, jobs, machines, max_operations):
        self.solver.solve(jobs, machines)

    def evaluate(self):
        pass

    def draw(self):
        pass
