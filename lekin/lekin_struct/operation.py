"""
Struct Operation/工序

property

method

"""


class OperationCollector:
    def __init__(self):
        self.operations = []  # List to store Operation objects

    def add_operation(self, operation):
        self.operations.append(operation)

    def get_operation_by_id(self, operation_id):
        for operation in self.operations:
            if operation.operation_id == operation_id:
                return operation
        return None


class Operation:
    def __init__(self, operation_id, operation_name, processing_time, demand_time, route_constraint):
        self.operation_id = operation_id
        self.operation_name = operation_name
        self.processing_time = processing_time
        self.demand_time = demand_time
        self.resource_requirements = []
        self.route_constraint = route_constraint
        self.earliest_start_time = None
        self.latest_start_time = None
        self.earliest_end_time = None
        self.latest_end_time = None

    def __str__(self):
        pass
