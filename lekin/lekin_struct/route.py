"""
Struct Route/工艺流程

property

method

"""

from typing import Any, Callable, Dict, List, Optional, Tuple

from lekin.lekin_struct.operation import Operation


class RouteCollector:
    def __init__(self):
        self.routes = {}

    def add_route(self, route):
        self.routes[route.route_id] = route

    def get_route_by_id(self, route_id):
        return self.routes.get(route_id, None)


class Route:
    def __init__(self, route_id, operations_sequence, available_resources=None):
        self.route_id = route_id
        self.operations_sequence = operations_sequence  # List of Operation objects
        self.available_resources = available_resources  # List of Resource objects representing available machines,
        # When assigning operations to resources, check for resource availability and consider resource capacities
        self.available_time_slots = []  # List of time slots when machines are available

    def add_operation(self, operation: Operation):
        self.operations.append(operation)

    def get_operations(self) -> List[Operation]:
        return self.operations

    def add_machine(self, machine):
        self.available_machines.append(machine)

    def add_time_slot(self, time_slot):
        self.available_time_slots.append(time_slot)

    # def __repr__(self):
    #     return (
    #         f"Route(route_id={self.route_id}, operation_ids={self.operation_ids},"
    #         f" resources_available={self.resources_available})"
    #     )
