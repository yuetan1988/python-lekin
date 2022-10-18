
import lekin
from lekin import Heuristics, Genetics
from lekin import Scheduler


job_list, machine_list = lekin.get_data('simple')
# job_list = lekin

solver = Heuristics('SPT')
scheduler = Scheduler(solver)
scheduler.solve(job_list, machine_list)

scheduler.draw()
