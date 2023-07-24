"""
backward + forward + push
"""

import pandas as pd

from lekin.dashboard.gantt import plot_gantt_chart
from lekin.lekin_struct import (
    Job,
    JobCollector,
    Operation,
    OperationCollector,
    Resource,
    ResourceCollector,
    Route,
    RouteCollector,
)
from lekin.solver.construction_heuristics.rule import BackwardScheduler

mo = pd.read_excel("./MOInput.xlsx", sheet_name="2.1.工单")
route_maps = pd.read_excel("./MOInput.xlsx", sheet_name="2.2.工艺路线")
resource_dates = pd.read_excel("./MOInput.xlsx", sheet_name="5.1.资源可用列表")

# print(mo)
# print(resource_dates)


job_collector = JobCollector()
for index, row in mo.iterrows():
    job_id = row["产品ID"]
    priority = row["优先级"]
    earliest_start_date = row["就绪时间"]
    demand_date = row["交付时间"]

    route_id = row["产品ID"]  # 这里用一样的，
    job_collector.add_job(
        Job(
            job_id=job_id,
            priority=priority,
            demand_time=demand_date,
            earliest_start_time=earliest_start_date,
            assigned_route_id=route_id,
        )
    )
print([i.job_id for i in job_collector.job_list])


operation_collector = OperationCollector()
route_collector = RouteCollector()
route_list = []
for group, row in route_maps.groupby("产品ID"):
    route_id = group
    operations_sequence = []
    print(row)

    for i, item in row.iterrows():
        operations_sequence.append(
            Operation(
                operation_id=row.loc[i, "工序ID"], operation_name=row.loc[i, "工序名称"], processing_time=row.loc[i, "任务基本时长"]
            )
        )

    route = Route(route_id=route_id, operations_sequence=operations_sequence)
    route_list.append(route)


print([i.route_id for i in route_list])
operations_sequence = route_list[0].operations_sequence
print([i.operation_id for i in operations_sequence])


operation_collector.get_operations_by_job_and_route(
    job_list=job_collector.job_list, route_id_list=job_collector.route_list
)


resource_collector = ResourceCollector()
for group, row in resource_dates.groupby("资源ID"):
    resource_id = group
    start_time = row["开始时间"]
    end_time = row["结束时间"]

    resource = Resource(resource_id=resource_id)
    for s, d in zip(start_time, end_time):
        resource.add_timeslot(start_time, end_time)
    resource_collector.add_resource(resource)

print([i.resource_id for i in resource_collector.get_all_resources()])


# scheduler = BackwardScheduler(job_collector, resource_collector)
# scheduler_result = scheduler.run()
