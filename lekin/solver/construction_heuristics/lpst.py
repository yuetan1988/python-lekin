"""Latest Possible Start Time
Backward scheduler
倒排"""


class LPSTScheduler:
    def __init__(self, jobs, routes):
        self.jobs = jobs
        self.routes = routes

    def calculate_lpst(self, operation):
        # Calculate the latest possible start time for an operation
        lpst = operation.due_date - operation.processing_time
        for successor in operation.successors:
            lpst = min(lpst, successor.lpst - successor.processing_time)
        return lpst

    def schedule_job(self, job):
        # Schedule the operations of a job based on LPST
        for operation in job.route.operations:
            operation.lpst = self.calculate_lpst(operation)
            operation.start_time = operation.lpst
            operation.end_time = operation.lpst + operation.processing_time

    def run(self):
        for job in self.jobs:
            self.schedule_job(job)
