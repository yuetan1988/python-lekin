def calculate_makespan(schedule_result):
    end_times = [end_time for (_, end_time) in schedule_result.values()]
    return max(end_times)


def calculate_flow_time(schedule_result, job):
    start_time, end_time = schedule_result[job.route.operations[-1]]
    return end_time - job.release_date


def calculate_changeover_time(schedule_result, job_collector):
    changeover_time = 0
    for resource in job_collector.resources:
        previous_end_time = 0
        for operation in schedule_result:
            if operation.resource == resource:
                changeover_time += max(0, operation.start_time - previous_end_time)
                previous_end_time = operation.end_time
    return changeover_time
