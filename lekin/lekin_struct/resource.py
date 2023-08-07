"""
Struct Machine/机器

property

method

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
import pandas as pd

from lekin.lekin_struct.timeslot import TimeSlot


class ResourceCollector:
    def __init__(self):
        self.resources = {}

    def add_resource(self, resource):
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
    def __init__(self, resource_id, resource_name=None, max_tasks=1):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.max_tasks = max_tasks  # maximum task can be done in same time, capacity
        self.tasks = {time_slot: None for time_slot in range(1, max_tasks + 1)}
        self.available_timeslots = []

        self.assigned_operation = []
        self.assigned_time_slot = []

    def add_timeslot(self, start_time, end_time):
        # self.available_timeslots.append(TimeSlot(self.resource_id, start_time, end_time))
        self.available_timeslots.append(TimeSlot(start_time, end_time))

    def assign_task(self, time_slot, operation):
        self.tasks[time_slot] = operation

    def get_task_at_time_slot(self, time_slot):
        return self.tasks.get(time_slot)

    def get_available_time_slots_within_time(self, start_time, limit_time, forward):
        available_hours = []
        current_hour = start_time

        pd.date_range(start_time, limit_time)

        while len(self.available_timeslots) > 0:
            if current_hour not in self.assigned_time_slot:
                available_hours.append(current_hour)
                # num_hours -= 1

            if forward:
                current_hour += 1
            else:
                current_hour -= 1

        return available_hours

    def get_unoccupied_time_slots(self):
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

    def __eq__(self, other):
        return

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return
