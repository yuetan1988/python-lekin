class SolverConfig:
    def __init__(self, entity_selector=None, move_selector=None, termination=None):
        self.entity_selector = entity_selector
        self.move_selector = move_selector
        self.termination = termination


class TerminationConfig:
    def __init__(self, seconds_spent_limit=None, max_iterations=None):
        self.seconds_spent_limit = seconds_spent_limit
        self.max_iterations = max_iterations
