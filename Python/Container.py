import agentpy as ap

class Container(ap.Agent):
    def __init__(self, field):
        self.field = field
        self.load = 0
        self.position = [0, 0]

    def loadContainer(self, amount):
        self.load += amount

    def move(self, newPosition):
        self.position = newPosition
