"""backward scheduling"""

import logging
import math

from lekin.lekin_struct.timeslot import TimeSlot
from lekin.solver.construction_heuristics.base import BaseScheduler


class BackwardScheduler(object):
    def __init__(self, job_collector, resource_collector, route_collector=None, **kwargs):
        self.job_collector = job_collector
        self.resource_collector = resource_collector
        self.route_collector = route_collector

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run(self):
        for i, job in enumerate(self.job_collector.job_list):
            self.scheduling_job(job, self.resource_collector, self.route_collector)
        logging.info("First Scheduling Done")
        return

    def scheduling_job(self, job, resource_collector, route_collector):
        logging.info(f"\nAssign Job {job.job_id}")

        if route_collector is not None:
            route_id = job.assigned_route_id
            route = None
            for r in route_collector:
                if r.route_id == route_id:
                    route = r
                    break
            if not route:
                print(f"Route with ID '{job.assigned_route_id}' not found for Job ID '{job.job_id}'. Skipping job.")

            job.operations = route.operations_sequence

        op_earliest_start = 0
        for operation in job.operations[::-1]:
            logging.info(f"\tAssign Operation {operation.operation_id} of Job {job.job_id}")
            chosen_resource, chosen_timeslot_hour = self.find_best_resource_and_timeslot_for_operation(
                operation, op_earliest_start
            )

            if chosen_resource and chosen_timeslot_hour:
                logging.info(
                    f"\tOperation {operation.operation_id} assigned in: resource"
                    f" {chosen_resource.resource_id}, {min(chosen_timeslot_hour)} -"
                    f" {max(chosen_timeslot_hour)}"
                )

                # assign
                operation.assigned_resource = chosen_resource
                operation.assigned_hours = chosen_timeslot_hour
                chosen_resource.assigned_operations.append(operation)
                chosen_resource.assigned_hours += chosen_timeslot_hour

                op_earliest_start = chosen_timeslot_hour[-1] + 1
        return

    def find_best_resource_and_timeslot_for_operation(self, operation, op_earliest_start, **kwargs):
        available_resource = operation.available_resource

        earliest_index = 0
        resource_earliest_time = float("inf")
        for i, resource in enumerate(available_resource):
            resource_time = resource.get_earliest_available_time(duration=operation.processing_time)

            if resource_time < resource_earliest_time:
                earliest_index = i
                resource_earliest_time = resource_time

        chosen_resource = available_resource[earliest_index]
        earliest_time = int(max(op_earliest_start, resource_earliest_time))
        chosen_hours = list(range(earliest_time, earliest_time + math.ceil(operation.processing_time)))
        return chosen_resource, chosen_hours

    def assign_operation(self, operation, start_time, end_time, resources):
        timeslot = TimeSlot(start_time, end_time)
        self.timeslots.append(timeslot)
        for resource in resources:
            # Add timeslot to resource's schedule
            resource.schedule.append(timeslot)
        # Link operation to scheduled timeslot
        operation.scheduled_timeslot = timeslot

    def select_resources(self, job, operation):
        available_slots = self.find_available_timeslots(job, operation)

        selected_resources = []
        for slot in available_slots:
            resources = slot.available_resources()
            resource = self.optimize_resource_selection(resources, operation)
            selected_resources.append((slot, resource))
        return selected_resources

    def find_available_timeslots(self, job, operation):
        # Search timeslots and filter based on:
        # - operation duration
        # - predecessor timeslots
        # - resource requirements

        slots = []
        # for ts in job.schedule.timeslots:
        #     if ts.end - ts.start >= operation.duration:
        #         if all(pred in job.predecessors(ts)):
        #             if ts.meets_resource_needs(operation):
        #                 slots.append(ts)
        return slots

    def optimize_resource_selection(self, resources, operation):
        # Score and prioritize resources based on:
        # - Capacity
        # - Changeover time
        # - Utilization

        scored = []
        for resource in resources:
            score = 0
            if resource.capacity >= operation.required_capacity:
                score += 1
            if resource.type in operation.preferred_resources:
                score += 1
            # Prioritize resources with less adjacent timeslots
            score -= len(resource.adjacent_timeslots(operation))
            scored.append((score, resource))
        best = max(scored, key=lambda x: x[0])
        return best[1]
