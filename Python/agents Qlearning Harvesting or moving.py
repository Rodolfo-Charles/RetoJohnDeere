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
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # Initialize Q-table with zeros
        self.q_table = np.zeros((self.rows, self.cols, 2))  # 2 actions: move or harvest

    def choose_action(self):
        if np.random.rand() < self.exploration_rate:
            # Explore: choose a random action (0: move, 1: harvest)
            return np.random.choice(2)
        else:
            # Exploit: choose the action with the highest Q-value
            row, col = self.position
            return np.argmax(self.q_table[row, col, :])

    def update_q_table(self, action, reward, next_position):
        row, col = self.position
        next_row, next_col = next_position

        # Update Q-value for the chosen action
        current_q_value = self.q_table[row, col, action]
        max_future_q_value = np.max(self.q_table[next_row, next_col, :])
        new_q_value = (1 - self.learning_rate) * current_q_value + \
                      self.learning_rate * (reward + self.discount_factor * max_future_q_value)

        self.q_table[row, col, action] = new_q_value


    def harvest(self):
        row, col = self.position
        if self.field[row][col] == 1:
            print(f"Harvester harvesting at position {self.position}")
            self.field[row][col] = 0
            self.tractor.loadContainer(1)
            return 1
        else:
            print(f"No crop at position {self.position}")
            return -1
    
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
        if self.field[row][col] == 1: return -2
        if self.field[row][col] == 0: return 1

    def run(self):
        cont = 0
        while self.position != (self.rows - 1, self.cols - 1):
            print('-------------------------------')
            
            # Choose action using Q-learning
            action = self.choose_action()

            if action == 0:  # Move
                reward = self.move()
                self.tractor.move(self.position)
                self.tractor.moveContainer(self.position)
            elif action == 1:  # Harvest
                reward = self.harvest()
                

            # Get the next state (position after the action)
            next_position = self.position

            # Update Q-table based on the reward and the next state
            reward = 1 if action == 1 else 0  # Reward for harvesting
            self.update_q_table(action, reward, next_position)

            # Save information for visualization
            dic[f"step{cont}"] = {
                'harvesterPosition': self.position,
                'tractorPosition': self.tractor.position,
                'containerPosition': self.tractor.container.position,
                'containerLoad': self.tractor.container.load,
                'field': [row[:] for row in self.field],
                'action': action,
                'reward': reward
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

# ... (rest of the code remains unchanged)




# Create the model
field_size = 10
field = [[1 for _ in range(field_size)] for _ in range(field_size)]

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