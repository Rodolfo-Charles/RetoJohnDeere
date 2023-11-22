from agentpy import Agent, Model
import numpy as np

dic = {}

class Tractor(Agent):
    def __init__(self, container, field):
        self.field = field
        self.container = container
        self.position = (0, 0)
        self.rows = len(field)
        self.cols = len(field[0])

    def move(self, newPosition):
        print(f"Tractor following harvester! {self.position}")
        self.position = newPosition

    def moveContainer(self, newPosition):
        self.container.move(newPosition)

    def loadContainer(self, amount):
        self.container.loadContainer(amount)


class Harvester(Agent):
    def __init__(self, tractor, field, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.field = field
        self.tractor = tractor
        self.position = (0, 0)
        self.rows = len(field)
        self.cols = len(field[0])

        # Q-learning parameters
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # Initialize Q-values table
        self.q_values = np.zeros((self.rows, self.cols, 4))  # 4 actions (up, down, left, right)

    def discretize_state(self, state):
        row, col = state
        return row, col

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(4)  # Explore: randomly choose an action
        else:
            return np.argmax(self.q_values[state[0], state[1]])

    def update_q_values(self, state, action, next_state, reward):
        current_q_value = self.q_values[state[0], state[1], action]
        max_future_q_value = np.max(self.q_values[next_state[0], next_state[1]])

        new_q_value = (1 - self.learning_rate) * current_q_value + \
                      self.learning_rate * (reward + self.discount_factor * max_future_q_value)

        self.q_values[state[0], state[1], action] = new_q_value

    def move(self):
        row, col = self.position
        state = self.discretize_state((row, col))
        action = self.choose_action(state)

        # Move to the next cell in the field based on the chosen action
        if action == 0 and row > 0:
            self.position = (row - 1, col)  # move up
        elif action == 1 and row < self.rows - 1:
            self.position = (row + 1, col)  # move down
        elif action == 2 and col > 0:
            self.position = (row, col - 1)  # move left
        elif action == 3 and col < self.cols - 1:
            self.position = (row, col + 1)  # move right

        return state, action

    def harvest(self):
        row, col = self.position
        if self.field[row][col] == 1:
            print(f"Harvester harvesting at position {self.position}")
            self.field[row][col] = 0
        else:
            print(f"No crop at position {self.position}")

    def run(self):
        cont = 0
        while (self.position != (self.rows - 1, self.cols - 1) and (self.field - np.zeros((10, 10))).any()):
            print('-------------------------------')
            state, action = self.move()
            self.harvest()
            self.tractor.loadContainer(1 if self.field[state[0]][state[1]] == 1 else 0 )
            self.tractor.move(self.position)
            self.tractor.moveContainer(self.position)

            next_state = self.discretize_state(self.position)
            reward = 1 if self.field[state[0]][state[1]] == 1 else 0  # Reward for harvesting

            self.update_q_values(state, action, next_state, reward)

            dic[f"step{cont}"] = {
                'harvesterPosition': self.position,
                'tractorPosition': self.tractor.position,
                'containerPosition': self.tractor.container.position,
                'containerLoad': self.tractor.container.load,
                'field': [row[:] for row in self.field],
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

    def move(self, newPosition):
        # Move to the next cell in the field
        print(f"Container attached to tractor! {self.position}")
        self.position = newPosition


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

# Run the model
harvesterAgent.run()

# Display the harvested field
print("Harvested field:")
for row in field:
    print(row)

print(dic)