import numpy as np

class Field:
    def __init__(self, size=10, num_obstacles=3):
        self.field = np.ones((size, size))
        # Add obstacles at random positions
        for _ in range(num_obstacles):
            while True:
                obstacle_position = np.random.randint(0, size, 2)
                if (obstacle_position == [0, 0]).all():  # Avoid placing obstacle at (0, 0)
                    continue
                if self.field[obstacle_position[0], obstacle_position[1]] != 2:  # Avoid placing obstacle on another obstacle
                    self.field[obstacle_position[0], obstacle_position[1]] = 2
                    break

    def print_field(self):
        print(self.field)

num_obstacles = 3
field = Field(num_obstacles=num_obstacles)

class Harvester:
    def __init__(self, field, alpha=0.5, gamma=0.6):
        self.field = field
        self.position = [0, 0]
        self.q_table = np.zeros((field.field.shape[0], field.field.shape[1], 4))  # Inicializar Q-Table
        self.alpha = alpha
        self.gamma = gamma

    def move(self):
        self.harvest()  # Harvest Starting Position
        while self.position[1] < self.field.field.shape[1] - 1:  # repeat until the top-right corner is reached
            # Move down until the end of the field
            while self.position[0] < self.field.field.shape[0] - 1:
                self.position[0] += 1
                self.harvest()
            # Move right
            if self.position[1] < self.field.field.shape[1] - 1:
                self.position[1] += 1
                self.harvest()
            # Move up until the top of the field
            while self.position[0] > 0:
                self.position[0] -= 1
                self.harvest()
            # Move right
            if self.position[1] < self.field.field.shape[1] - 1:
                self.position[1] += 1
                self.harvest()

            # Q-Learning when obstacle
            action = np.argmax(self.q_table[self.position[0], self.position[1]])
            old_position = self.position.copy()
            if action == 0:   # Up
                self.position[0] = max(0, self.position[0] - 1)
            elif action == 1: # Down
                self.position[0] = min(self.field.field.shape[0] - 1, self.position[0] + 1)
            elif action == 2: # Left
                self.position[1] = max(0, self.position[1] - 1)
            elif action == 3: # Right
                self.position[1] = min(self.field.field.shape[1] - 1, self.position[1] + 1)
            # Update Q-table
            reward = -10 if self.field.field[self.position[0], self.position[1]] == 2 else 1
            old_q_value = self.q_table[old_position[0], old_position[1], action]
            max_future_q_value = np.max(self.q_table[self.position[0], self.position[1]])
            new_q_value = (1 - self.alpha) * old_q_value + self.alpha * (reward + self.gamma * max_future_q_value)
            self.q_table[old_position[0], old_position[1], action] = new_q_value

    def harvest(self):
        if self.field.field[self.position[0], self.position[1]] == 1:
            self.field.field[self.position[0], self.position[1]] = 0

harvester = Harvester(field)

print("Initial field:")
field.print_field()

harvester.move()

print("Field after harvesting:")
field.print_field()

if np.sum(field.field) == 2 * num_obstacles:
    print("Successful: All crops were harvested!")
else:
    print("Fail: Not all crops were harvested.")
