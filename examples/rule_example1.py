import json

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
from lekin.solver.construction_heuristics import LPSTScheduler, SPTScheduler


def prepare_data(file_path="./data/k1.json"):
    with open(file_path, "r", encoding="utf8") as file:  # read file from path
        data = json.loads(file.read())

    job_collector = JobCollector()
    # operation_collector = OperationCollector()
    route_collector = RouteCollector()
    resource_collector = ResourceCollector()

    if list(data.keys()) == ["itineraries", "machines"]:
        resources = data["machines"]  # is first level structure is correct, then split
        routes = data["itineraries"]

        # parse the resource
        for re in resources:
            re_name = re["machineName"]
            re_id = int(re_name.replace("M", ""))
            resource = Resource(resource_id=re_id, resource_name=re_name)
            resource_collector.add_resource_dict({re_id: resource})
        print([i.resource_id for i in resource_collector.get_all_resources()])

        # parse the job and route
        for ro in routes:
            # ro_name = ro["itineraryName"]
            ro_id = int(ro["itineraryName"].replace("Itinerary ", ""))
            route = Route(route_id=ro_id)
            operations_sequence = []
            for ta in ro["tasksList"]:
                op_name = ta["taskName"]
                op_id = ta["taskName"].replace("Task ", "")

                op_pt = ta["taskDuration"]

                op_tm = []
                if isinstance(ta["taskMachine"], list):
                    for re in ta["taskMachine"]:
                        re_name = re["machineName"]
                        re_id = int(re_name.replace("M", ""))
                        op_tm.append(Resource(resource_id=re_id, resource_name=re_name))
                else:
                    re_name = ta["taskMachine"]["machineName"]
                    re_id = int(re_name.replace("M", ""))
                    op_tm.append(Resource(resource_id=re_id, resource_name=re_name))

                operations_sequence.append(
                    Operation(
                        operation_id=op_id,
                        operation_name=op_name,
                        quantity=1,
                        processing_time=op_pt,
                        parent_job_id=ro_id,  # route defines job here
                        available_resource=op_tm,
                    )
                )

            route.operations_sequence = operations_sequence
            route_collector.add_route(route)

            job_collector.add_job(Job(job_id=ro_id, assigned_route_id=ro_id))

        # print(resources)
        print(routes)
        pass
    return job_collector, route_collector, resource_collector


def run_scheduling(job_collector, route_list, resource_collector):
    scheduler = SPTScheduler()
    scheduler.solve(job_collector, resource_collector, route_list)
    return


if __name__ == "__main__":
    prepare_data(file_path="./data/k1.json")
