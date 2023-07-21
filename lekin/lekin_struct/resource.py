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

from lekin.lekin_struct.timeslot import TimeSlot


class ResourceCollector:
    def __init__(self):
        self.resources = {}

    def add_resource(self, resource):
        self.resources[resource.resource_id] = resource

    def get_resource(self, resource_id):
        return self.resources.get(resource_id)

    def get_all_resources(self):
        return list(self.resources.values())

    def get_unoccupied_time_slots(self):
        unoccupied_slots = []
        for resource in self.get_all_resources():
            unoccupied_slots.extend(resource.get_unoccupied_time_slots())
        return unoccupied_slots


class Resource:
    def __init__(self, resource_id, resource_name):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.available_timeslots = []

    def add_timeslot(self, start_time, end_time):
        self.available_timeslots.append(TimeSlot(self.resource_id, start_time, end_time))

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

    def __eq__(self, other):
        return

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return
