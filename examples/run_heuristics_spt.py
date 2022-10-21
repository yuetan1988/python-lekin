import lekin
from lekin import Genetics, Heuristics, Scheduler

job_list, machine_list = lekin.get_data("simple")
# job_list = lekin

solver = Heuristics("SPT")
scheduler = Scheduler(solver)
scheduler.solve(job_list, machine_list)

scheduler.draw()
