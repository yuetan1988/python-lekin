class SolverConfig:
    def __init__(self):
        self.entity_selector = None
        self.move_selector = None
        self.termination = None


class TerminationConfig:
    def __init__(self, seconds_spent_limit):
        self.seconds_spent_limit = seconds_spent_limit
