"""forward scheduling"""

import logging

from lekin.solver.construction_heuristics.base import BaseScheduler


class ForwardScheduler(BaseScheduler):
    def __init__(self, job_collector, resource_collector, route_collector=None, **kwargs):
        super().__init__(job_collector, resource_collector, **kwargs)
        self.job_collector = job_collector
        self.resource_collector = resource_collector
        self.route_collector = route_collector

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run(self):
        for i, job in enumerate(self.job_collector):
            self.scheduling_job(job, self.resource_collector)
        return

    def scheduling_job(self, job, resource_collector):
        logging.info(f"Assign Job {job.job_id}")

        for operation in job.operations:
            logging.info(f"\tAssign Operation {operation.operation_id} of Job {job.job_id}")
            chosen_resource, chosen_timeslot_hour = self.find_best_resource_and_timeslot_for_operation(operation)

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
                chosen_resource.assigned_hours.append(chosen_timeslot_hour)

                # latest_end_time = chosen_timeslot_hour[0]
        return

    def rescheduling_job(self, job):
        return

    def find_best_resource_and_timeslot_for_operation(self, operation, **kwargs):
        return
