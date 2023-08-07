"""
资源日历
"""

from datetime import datetime, timedelta

import pandas as pd


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

    @property
    def hours(self):
        return pd.date_range(start=self.start_time, end=self.end_time, freq="1H")

    @property
    def num_of_hours(self):
        return len(pd.date_range(start=self.start_time, end=self.end_time, freq="1H"))


# class TimeSlot:
#     def __init__(self, resource_id, start_time, end_time):
#         self.resource_id = resource_id
#         self.start_time = start_time
#         self.end_time = end_time
