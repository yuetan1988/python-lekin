"""backward scheduling"""
from lekin.lekin_struct.timeslot import TimeSlot


class BackwardScheduler(object):
    def __init__(self):
        pass

    def run(self):
        return


class AdvBackwardScheduler(object):
    """
    chose the resource based on configurable choices
    """

    def __init__(self):
        pass

    def run(self):

        return

    def assign_operation(self, operation, start_time, end_time, resources):
        timeslot = TimeSlot(start_time, end_time)
        self.timeslots.append(timeslot)
        for resource in resources:
            # Add timeslot to resource's schedule
            resource.schedule.append(timeslot)
        # Link operation to scheduled timeslot
        operation.scheduled_timeslot = timeslot

    def select_resources(self, job, operation):
        available_slots = self.find_available_timeslots(job, operation)

        selected_resources = []
        for slot in available_slots:
            resources = slot.available_resources()
            resource = self.optimize_resource_selection(resources, operation)
            selected_resources.append((slot, resource))
        return selected_resources

    def find_available_timeslots(self, job, operation):
        # Search timeslots and filter based on:
        # - operation duration
        # - predecessor timeslots
        # - resource requirements

        slots = []
        # for ts in job.schedule.timeslots:
        #     if ts.end - ts.start >= operation.duration:
        #         if all(pred in job.predecessors(ts)):
        #             if ts.meets_resource_needs(operation):
        #                 slots.append(ts)
        return slots

    def optimize_resource_selection(self, resources, operation):
        # Score and prioritize resources based on:
        # - Capacity
        # - Changeover time
        # - Utilization

        scored = []
        for resource in resources:
            score = 0
            if resource.capacity >= operation.required_capacity:
                score += 1
            if resource.type in operation.preferred_resources:
                score += 1
            # Prioritize resources with less adjacent timeslots
            score -= len(resource.adjacent_timeslots(operation))
            scored.append((score, resource))
        best = max(scored, key=lambda x: x[0])
        return best[1]
