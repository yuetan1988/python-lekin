"""
Local search
https://towardsdatascience.com/optimization-techniques-tabu-search-36f197ef8e25
"""


import math
import random


class TabuSearchScheduler:
    def __init__(self, job_collector, max_iterations=1000, tabu_size=20):
        self.job_collector = job_collector
        self.max_iterations = max_iterations
        self.tabu_size = tabu_size

    def schedule(self):
        best_solution = self.generate_initial_solution()
        best_cost = self.calculate_cost(best_solution)

        tabu_list = [best_solution]
        current_solution = best_solution

        for iteration in range(self.max_iterations):
            neighbors = self.generate_neighbors(current_solution)
            non_tabu_neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]

            if not non_tabu_neighbors:
                break

            current_solution = random.choice(non_tabu_neighbors)
            current_cost = self.calculate_cost(current_solution)

            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

            tabu_list.append(current_solution)
            if len(tabu_list) > self.tabu_size:
                tabu_list.pop(0)

        return best_solution

    def generate_initial_solution(self):
        # Randomly assign operations to time slots
        solution = {}
        for job in self.job_collector.jobs:
            for operation in job.route.operations:
                solution[(job.id, operation.id)] = random.randint(
                    0, self.job_collector.max_time - operation.processing_time
                )
        return solution

    def generate_neighbors(self, solution):
        neighbors = []
        for i in range(len(solution)):
            neighbor = solution.copy()
            job_id, operation_id = list(neighbor.keys())[i]
            operation = self.job_collector.get_operation_by_id(job_id, operation_id)
            neighbor[(job_id, operation_id)] = random.randint(
                0, self.job_collector.max_time - operation.processing_time
            )
            neighbors.append(neighbor)
        return neighbors

    def calculate_cost(self, solution):
        # Calculate the makespan of the schedule
        max_end_time = 0
        for job in self.job_collector.jobs:
            end_time = max(
                [solution[(job.id, operation.id)] + operation.processing_time for operation in job.route.operations]
            )
            max_end_time = max(max_end_time, end_time)
        return max_end_time
