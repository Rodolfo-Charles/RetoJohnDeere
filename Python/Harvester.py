import agentpy as ap
import numpy as np
class Harvester(ap.Agent):
	def __init__(self, field, q_values):
		self.field = field
		self.position = [1, 1]
		self.rows = len(field)
		self.cols = len(field[0])
		self.actions = ['up', 'right', 'down', 'left']
		self.q_values = q_values



	#define an epsilon greedy algorithm that will choose which action to take next (i.e., where to move next)
	def get_next_action(self, current_row_index, current_column_index, epsilon):
		#if a randomly chosen value between 0 and 1 is less than epsilon,
		#then choose the most promising value from the Q-table for this state.
		if np.random.random() < epsilon:
			return np.argmax(self.q_values[current_row_index, current_column_index])
		else: #choose a random action
			return np.random.randint(4)

	#define a function that will get the next location based on the chosen action
	def get_next_location(self, current_row_index, current_column_index, action_index):
		new_row_index = current_row_index
		new_column_index = current_column_index
		if self.actions[action_index] == 'up' and current_row_index > 0:
			new_row_index -= 1
		elif self.actions[action_index] == 'right' and current_column_index < self.cols - 1:
			new_column_index += 1
		elif self.actions[action_index] == 'down' and current_row_index < self.rows - 1:
			new_row_index += 1
		elif self.actions[action_index] == 'left' and current_column_index > 0:
			new_column_index -= 1

		self.position = [new_row_index, new_column_index]
		return new_row_index, new_column_index


	def harvest(self):
		if self.field[self.position[0], self.position[1]] == 1:
			self.field[self.position[0], self.position[1]] = -1