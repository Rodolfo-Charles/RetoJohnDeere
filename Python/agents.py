from agentpy import Agent, Model

dic = {}
class Tractor(Agent):
    def __init__(self, container, field):
        self.field = field
        self.container = container
        self.position = (0, 0)
        self.rows = len(field)
        self.cols = len(field[0])

    def move(self):
        # Move to the next cell in the field
        print(f"Tractor following harvester! {self.position}")
        row, col = self.position
        if col < self.cols - 1:
            self.position = (row, col + 1)
        elif row < self.rows - 1:
            self.position = (row + 1, 0)
        else:
            # Tractor has reached the end of the field
            print("Tractor has reached the end of the field!")

    def moveContainer(self):
        self.container.move()

    def loadContainer(self, amount):
        self.container.loadContainer(amount)

class Harvester(Agent):
    def __init__(self, tractor, field):
        self.field = field
        self.tractor = tractor
        self.position = (0, 0)
        self.rows = len(field)
        self.cols = len(field[0])

    def move(self):
        # Move to the next cell in the field
        row, col = self.position
        if col < self.cols - 1:
            self.position = (row, col + 1)
        elif row < self.rows - 1:
            self.position = (row + 1, 0)
        else:
            # Harvester has reached the end of the field
            print("Harvester has finished harvesting!")

    def harvest(self):
        row, col = self.position
        if self.field[row][col] == 1:
            print(f"Harvester harvesting at position {self.position}")
            self.field[row][col] = 0
        else:
            print(f"No crop at position {self.position}")

    def run(self):
        cont = 0
        while self.position != (self.rows - 1, self.cols - 1):
            print('-------------------------------')
            self.harvest()
            self.tractor.loadContainer(1)
            self.move()
            self.tractor.move()
            self.tractor.moveContainer()

            dic[f"step{cont}"] = {
                'harvesterPosition': self.position,
                'tractorPosition': self.tractor.position,
                'containerPosition': self.tractor.container.position,
                'containerLoad': self.tractor.container.load,
                'field': [row[:] for row in self.field]

            }
            cont += 1



class Container(Agent):
    def __init__(self, field):
        self.field = field
        self.load = 0
        self.position = (0, 0)
        self.rows = len(field)
        self.cols = len(field[0])

    def loadContainer(self, amount):
        self.load += amount
        print(f"Container loaded from harvester! {self.load}")


    def move(self):
        # Move to the next cell in the field
        print(f"Container attached to tractor! {self.position}")
        print(self.position)
        row, col = self.position
        if col < self.cols - 1:
            self.position = (row, col + 1)
        elif row < self.rows - 1:
            self.position = (row + 1, 0)
        else:
            # Tractor has reached the end of the field
            print("Tractor has reached the end of the field!")

# Create the model
field_size = 10
field = [[1 for _ in range(field_size)] for _ in range(field_size)]

container = Container(field)
tractor = Tractor(container, field)
harvesterAgent = Harvester(tractor, field)


# Display the initial field
print("Initial field:")
for row in field:
    print(row)

# run model
harvesterAgent.run()

# Display the initial field
print("Harvested field:")
for row in field:
    print(row)

print(dic)


# Version 1:
# falta agregar q-learning a los movimientos y agregar obstaculos + esquivarlos