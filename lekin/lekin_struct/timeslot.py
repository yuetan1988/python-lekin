"""
资源日历
"""


class TimeSlot:
    def __init__(self, resource_id, start_time, end_time):
        self.resource_id = resource_id
        self.start_time = start_time
        self.end_time = end_time
