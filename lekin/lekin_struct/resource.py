"""
Resource/Machine Struct

# Assume we have a list of resource IDs
resource_ids = [1, 2, 3]

# Create a ResourceCollector
resource_collector = ResourceCollector()

# Function to add time slots to a resource
def add_time_slots_to_resource(resource, start_times, processing_times):
    for start_time, processing_time in zip(start_times, processing_times):
        end_time = start_time + timedelta(hours=processing_time)
        resource.add_time_slot(start_time, end_time)

# Example time slot data (start times and processing times)
resource1_start_times = [datetime(2023, 7, 25, 8, 0), datetime(2023, 7, 25, 14, 0)]
resource1_processing_times = [2, 3]

resource2_start_times = [datetime(2023, 7, 25, 10, 0)]
resource2_processing_times = [4]

resource3_start_times = [datetime(2023, 7, 25, 9, 0), datetime(2023, 7, 25, 13, 0)]
resource3_processing_times = [2, 2.5]

# Add resources to the ResourceCollector
for resource_id in resource_ids:
    resource = Resource(resource_id)
    resource_collector.add_resource(resource)

# Get each resource and add time slots
resource1 = resource_collector.get_resource(1)
resource2 = resource_collector.get_resource(2)
resource3 = resource_collector.get_resource(3)

add_time_slots_to_resource(resource1, resource1_start_times, resource1_processing_times)
add_time_slots_to_resource(resource2, resource2_start_times, resource2_processing_times)
add_time_slots_to_resource(resource3, resource3_start_times, resource3_processing_times)
"""

import math

import pandas as pd

from lekin.lekin_struct.timeslot import TimeSlot


class ResourceCollector:
    def __init__(self):
        self.resources = {}

    def add_resource_dict(self, resource):
        self.resources.update(resource)

    def get_resource_by_id(self, resource_id):
        return self.resources.get(resource_id)

    def get_all_resources(self):
        return list(self.resources.values())

    def get_unoccupied_time_slots(self):
        unoccupied_slots = []
        for resource in self.get_all_resources():
            unoccupied_slots.extend(resource.get_unoccupied_time_slots())
        return unoccupied_slots


class Resource:
    def __init__(self, resource_id, resource_name=None, max_tasks=1, **kwargs):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.max_tasks = max_tasks  # maximum task can be done in same time, capacity
        self.tasks = {time_slot: None for time_slot in range(1, max_tasks + 1)}
        self.available_timeslots = []

        self.assigned_operation = []
        self.assigned_time_slot = []

        for key, value in kwargs.items():
            setattr(self, key, value)

    def add_timeslot(self, start_time, end_time):
        # self.available_timeslots.append(TimeSlot(self.resource_id, start_time, end_time))
        self.available_timeslots.append(TimeSlot(start_time, end_time))

    def assign_task(self, time_slot, operation):
        self.tasks[time_slot] = operation

    def get_task_at_time_slot(self, time_slot):
        return self.tasks.get(time_slot)

    def get_available_time_slots_within_time(self, start=None, end=None, periods=None, freq="1H", forward=True):
        available_hours = []

        # check_periods = pd.date_range(start=start, end=end, periods=periods, freq=freq)
        # if not forward:
        #     check_periods = check_periods[::-1]
        # occupied_periods = [i.hours for i in self.assigned_time_slot]
        # for period in check_periods:
        #     if period not in occupied_periods:
        #         available_hours.append(period)
        #     else:  # considering the continuous assignment
        #         break

        # all_available_end_time = [slot.end_time for slot in self.available_timeslots]
        # just_in_time_end_time_slot = max([i for i in all_available_end_time if i <= end])
        if forward:
            selected_time_slot = [i for i in self.available_timeslots if i.start_time >= start]
        else:
            selected_time_slot = [i for i in self.available_timeslots if i.end_time <= end][::-1]

        # print(just_in_time_end_time_slot)
        # print([i.start_time for i in self.available_timeslots])
        # print([i.end_time for i in self.available_timeslots])
        # print(self.available_timeslots[0].hours)

        left_periods = periods

        for time_slot in selected_time_slot:
            if left_periods <= 0:
                break

            if start and time_slot.start_time < start:
                continue

            if end and time_slot.start_time >= end:
                break

            # if forward:
            #     current_time = max(start, time_slot.start_time)
            # else:
            #     current_time = min(end, time_slot.end_time)

            if time_slot in self.assigned_time_slot:
                break

            if time_slot.duration_of_hours < left_periods:
                available_hours += time_slot.hours
                left_periods -= time_slot.duration_of_hours

            else:
                available_hours += time_slot.hours[-math.ceil(left_periods) :]
                break
            #
            # print(left_periods, available_hours)

            # for current_time in range(max(start, time_slot.start_time),
            #                           min(end, time_slot.end_time - period) + 1):
            #     if all(self.is_available(current_time + offset, current_time +offset+1) for offset in range(periods)):
            #         available_hours.append(current_time)

        return available_hours

    def is_available(self, start_time, end_time):
        for assigned_time_slot in self.assigned_time_slots:
            if not (end_time <= assigned_time_slot.start_time or start_time >= assigned_time_slot.end_time):
                return False
        return True

    def get_unoccupied_time_slots_within_time(self):
        unoccupied_slots = []
        prev_end_time = None
        for time_slot in self.time_slots:
            if not time_slot.is_occupied():
                if prev_end_time:
                    # Check if there is a gap between unoccupied time slots
                    if time_slot.start_time > prev_end_time:
                        unoccupied_slots.append(TimeSlot(prev_end_time, time_slot.start_time))
                unoccupied_slots.append(time_slot)
                prev_end_time = time_slot.end_time
        return unoccupied_slots

    def merge_schedules(self):
        # Sort timeslots based on start time
        self.timeslots.sort(key=lambda x: x.start_time)

        merged_slots = []
        current_slot = None

        for slot in self.timeslots:
            if not current_slot:
                current_slot = slot
            else:
                # If the current slot and the next slot overlap, merge them
                if current_slot.end_time >= slot.start_time:
                    current_slot.end_time = max(current_slot.end_time, slot.end_time)
                else:
                    merged_slots.append(current_slot)
                    current_slot = slot

        if current_slot:
            merged_slots.append(current_slot)

        self.timeslots = merged_slots

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"{self.resource_id}"

    def __eq__(self, other):
        return self.resource_id == other.resource_id

    def __lt__(self, other):
        return self.resource_id < other.resource_id
