"""
backward + forward + push
"""

import pandas as pd

from lekin.lekin_struct import Job, JobCollector, Resource, ResourceCollector, Route
from lekin.solver.construction_heuristics.rule import BackwardScheduler

mo = pd.read_excel("./MOInput.xlsx", sheet_name="2.1.工单")
resource_date = pd.read_excel("./MOInput.xlsx", sheet_name="5.1.资源可用列表")

# print(mo)
print(resource_date)


job_collector = JobCollector()
for index, row in mo.iterrows():
    job_id = row["产品ID"]
    priority = row["优先级"]
    earliest_start_date = row["任务开始控制"]
    demand_date = row["交付时间"]
    assigned_route = map()
    # route_id = row['route_id']
    job_collector.add_job(
        Job(
            job_id=job_id,
            priority=priority,
            demand_time=demand_date,
            earliest_start_time=earliest_start_date,
            assigned_route=assigned_route,
        )
    )


resource_collector = ResourceCollector()
for group, row in resource_date.groupby("资源ID"):
    resource_id = group
    start_time = row["开始时间"]
    end_time = row["结束时间"]

    resource = Resource(resource_id=resource_id)
    for s, d in zip(start_time, end_time):
        resource.add_timeslot(start_time, end_time)
    resource_collector.add_resource(resource)


# scheduler = BackwardScheduler(job_collector, resource_collector)
# scheduler.run()
