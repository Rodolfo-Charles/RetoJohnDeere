import agentpy as ap
class Tractor(ap.Agent):
    def __init__(self, container, field):
        self.field = field
        self.container = container
        self.position = [1, 1]
        self.rows = len(field)
        self.cols = len(field[0])

    def move(self, newPosition):
        self.position = newPosition
        self.moveContainer(newPosition)

    def moveContainer(self, newPosition):
        self.container.move(newPosition)

    def loadContainer(self, amount):
        self.container.loadContainer(amount)
