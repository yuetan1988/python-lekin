"""
Struct Route/工艺流程

property

method

"""


class Route:
    def __init__(self, route_id):
        self.route_id = route_id
        self.operations = []  # List of Operation objects
        self.available_machines = []  # List of Resource objects representing available machines
        self.available_time_slots = []  # List of time slots when machines are available

    def add_operation(self, operation):
        self.operations.append(operation)

    def add_machine(self, machine):
        self.available_machines.append(machine)

    def add_time_slot(self, time_slot):
        self.available_time_slots.append(time_slot)
