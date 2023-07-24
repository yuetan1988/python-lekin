from datetime import datetime, timedelta
import heapq
from typing import Any, Callable, Dict, List, Optional, Tuple

from lekin.lekin_struct import Job, Operation, Resource, TimeSlot


class BackwardScheduler(object):
    def __init__(self):
        self.resource_occupancy = {}  # Resource occupancy schedule {resource_id: [(start_time, end_time)]}
        self.jobs_collector = {}  # Dictionary to store jobs by ID
        self.routes = {}  # Dictionary to store routes by ID
        self.assigned_timeslots = {}  # Dictionary to store assigned timeslots

    def backward_schedule(self, job_collector):
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

                # After the scheduling is done, fill in the assigned resource and time slot for each operation
                if operation.assigned_resource and operation.assigned_time_slot:
                    resource = self.resources[operation.assigned_resource]
                    resource.assign_task(operation.assigned_time_slot, operation)

    def find_available_timeslot(self, resource: Resource, operation: Operation):
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

    # 以下是为了push推紧，但是推紧的时候需要考虑工序之间的关联
    def forward_schedule(self):
        # push the unoccupied time slots and make the queue of operations continuous,
        # The forward scheduling will try to fill in the unoccupied time slots with operations
        # Get all the unoccupied time slots for each resource
        unoccupied_slots = self.get_unoccupied_time_slots()

        # Sort the unoccupied time slots in ascending order of start time
        unoccupied_slots.sort(key=lambda slot: slot.start_time)

        # Iterate through the unoccupied time slots and assign operations to fill them
        for slot in unoccupied_slots:
            for job in self.job_collector.jobs:
                for route_id in job.route_ids:
                    operations = self.job_collector.get_operations_by_job_and_route(job.job_id, route_id)
                    for operation in operations:
                        start_time, end_time = self.find_available_timeslot(slot.resource, operation, slot.start_time)
                        if start_time is not None and end_time is not None:
                            self.assign_to_resource(slot.resource, operation, start_time, end_time)
                            break  # Stop iterating through operations once the time slot is filled
                if slot.is_occupied():
                    break  # Stop iterating through jobs if the time slot is filled

    def get_unoccupied_time_slots(self):
        unoccupied_slots = []
        for resource in self.job_collector.resources:
            for slot in resource.available_timeslots:
                if not slot.is_occupied():
                    unoccupied_slots.append(slot)
        return unoccupied_slots

    # 便于保存结果
    def assign_operation(self, operation, resource):
        # Check if the resource has any available time slots for the operation
        resource_time_slots = resource.get_time_slots()
        for time_slot in resource_time_slots:
            if time_slot.start_time <= operation.get_max_begin():
                # Assign the operation to the resource within the available time slot
                operation.assign_resource(resource, time_slot)
                operation.assigned_resource = resource  # Update the assigned resource
                operation.assigned_time_slot = time_slot  # Update the assigned time slot
                return True
        return False

    # 排序时不光考虑priority，也考虑连续性和时间差，也就是时间差不多的排序时就排在一起
    def sort_jobs(self, jobs: List[Job]):
        # Custom sorting function based on priority and continuity
        def custom_sort(job):
            priority_weight = job.priority  # You may adjust the weight based on your requirements
            continuity_weight = -self.calculate_gap_time(job)
            return priority_weight + continuity_weight

        return sorted(jobs, key=custom_sort, reverse=True)

    def calculate_gap_time(self, job: Job):
        # Calculate the gap time between consecutive jobs of the same type
        jobs_same_type = [j for j in self.job_collector.get_jobs_by_type(job.type)]
        jobs_same_type.sort(key=lambda j: j.demand_date)
        gap_times = [
            jobs_same_type[i + 1].demand_date - jobs_same_type[i].demand_date for i in range(len(jobs_same_type) - 1)
        ]
        return max(gap_times) if gap_times else 0

    # 考虑换型时间
    def assign_operation_changeover(self, operation, resource, start_time):
        # Calculate end time based on setup time and processing time
        setup_time = 0
        if resource:
            setup_time = operation.setup_time  # Get the setup time for this operation and resource
        end_time = start_time + setup_time + operation.processing_time

        # Check if the resource is available during the entire operation duration
        if self.is_resource_available(resource, start_time, end_time):
            # Assign the operation to the resource and update its start and end times
            operation.required_resource = resource
            operation.start_time = start_time + setup_time
            operation.end_time = end_time
            # Update resource availability
            self.update_resource_availability(resource, start_time + setup_time, end_time)
            return True
        else:
            return False

    # 换型
    def schedule_jobs_changeover(self, jobs):
        sorted_jobs = self.sort_jobs_by_priority(jobs)
        for job in sorted_jobs:
            current_resource = None
            current_end_time = job.demand_date

            for operation in job.route.operations[::-1]:  # Reverse order
                # Calculate the start time for the current operation
                start_time = current_end_time - operation.processing_time

                # If the operation has a next operation, consider the setup time
                if operation.next_operation:
                    setup_time = self.get_setup_time(operation, current_resource)
                    start_time -= setup_time

                # Assign the operation to a resource
                assigned = False
                for resource in self.resources:
                    assigned = self.assign_operation(operation, resource, start_time)
                    if assigned:
                        current_resource = resource
                        current_end_time = start_time
                        break

                if not assigned:
                    raise ValueError("Operation could not be scheduled on any available resource.")
