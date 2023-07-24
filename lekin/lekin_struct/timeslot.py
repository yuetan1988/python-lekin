"""
资源日历
"""

from datetime import datetime, timedelta


class TimeSlot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = end_time - start_time
        self.assigned_operation = None

    def assign_operation(self, operation, processing_time):
        self.assigned_operation = operation
        self.end_time = self.start_time + timedelta(hours=processing_time)

    def is_occupied(self):
        return self.assigned_operation is not None


# class TimeSlot:
#     def __init__(self, resource_id, start_time, end_time):
#         self.resource_id = resource_id
#         self.start_time = start_time
#         self.end_time = end_time
