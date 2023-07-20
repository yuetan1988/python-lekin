"""
Struct Machine/机器

property

method

"""

from lekin.lekin_struct.timeslot import TimeSlot


class Resource:
    def __init__(self, resource_id, resource_name):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.available_timeslots = []

    def add_timeslot(self, start_time, end_time):
        self.available_timeslots.append(TimeSlot(self.resource_id, start_time, end_time))

    def __eq__(self, other):
        return

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return
