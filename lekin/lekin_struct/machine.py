"""
Struct Machine

"""


class Machine(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return
