from datetime import datetime, timedelta
import heapq

from lekin.lekin_struct import Job, Operation, TimeSlot


class BackwardScheduler(object):
    def __init__(self):
        self.resource_occupancy = {}  # Resource occupancy schedule {resource_id: [(start_time, end_time)]}
        self.jobs_collector = {}  # Dictionary to store jobs by ID
        self.routes = {}  # Dictionary to store routes by ID
        self.assigned_timeslots = {}  # Dictionary to store assigned timeslots

    def solve(self, job_collector):
        # Sort jobs based on priority (higher priority first)
        jobs_collector = job_collector.jobs
        jobs_collector.sort(key=lambda x: x.priority, reverse=True)

        for job in jobs_collector:
            route = None
            for r in self.routes:
                if r.route_id == job.route_id:
                    route = r
                    break
            if not route:
                print(f"Route with ID '{job.route_id}' not found for Job ID '{job.job_id}'. Skipping job.")
                continue

            operations = route.operations[::-1]  # Reverse the operations in the route
            for operation in operations:
                # Find available timeslot for the current operation
                priority_resources = operation.priority_resources

                # Iterate through the priority resources to find an available time slot
                for resource in priority_resources:
                    start_time, end_time = self.find_available_timeslot(resource, operation)

                    if not end_time:
                        # print(
                        #     f"No available timeslot found for Operation ID '{operation.operation_id}' in Job ID"
                        #     f" '{job.job_id}'."
                        # )
                        break

                    self.assign_to_resource(resource, operation, start_time, end_time)
                    # print(
                    #     f"Assigned Operation ID '{operation.operation_id}' to Timeslot: {cur_time} -"
                    #     f" {timeslot.end_time}"
                    # )

    def find_available_timeslot(self, resource, operation):
        job_type = operation.job.job_type
        existing_operations = [op for op in resource.assigned_operations if op.job.job_type == job_type]
        existing_operations.sort(key=lambda op: op.end_time, reverse=True)

        processing_time = self.calculate_processing_time(operation)

        # If there are existing operations, find the next available time slot after the last operation's end time
        if existing_operations:
            last_operation = existing_operations[0]
            if last_operation.end_time + timedelta(hours=processing_time) <= operation.demand_date:
                start_time = operation.demand_date
            else:
                start_time = last_operation.end_time + timedelta(hours=1)  # Add a buffer time between operations
        else:
            start_time = operation.demand_date

        for slot in resource.available_timeslots:
            if slot.start_time <= start_time and slot.end_time >= start_time + timedelta(hours=processing_time):
                return start_time, start_time + timedelta(hours=processing_time)
        return

    def find_assigned_timeslot(self, job_id, operation_id):
        # Find the assigned timeslot for a specific operation in a job (if any).
        key = (job_id, operation_id)
        return self.assigned_timeslots.get(key, None)

    def assign_timeslot(self, job_id, operation_id, timeslot):
        # Assign a timeslot to a specific operation in a job.
        key = (job_id, operation_id)
        self.assigned_timeslots[key] = timeslot
