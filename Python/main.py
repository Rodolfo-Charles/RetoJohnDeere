import numpy as np
from Harvester import Harvester
from Tractor import Tractor
from Container import Container
from Field import Field
import json


environmentRows = 11
environmentColumns = 11
field = np.full((environmentRows, environmentColumns), 1)

q_values = np.zeros((environmentRows, environmentColumns, 4))

fieldAgent = Field(field, environmentRows, environmentColumns)
actions = ['up', 'right', 'down', 'left']

indicesToChange = fieldAgent.getIndicesToChange(4)
field = fieldAgent.createObstacles(indicesToChange)

for row in field:
  print(row)
#define training parameters
epsilon = 0.9 #the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9 #discount factor for future rewards
learning_rate = 0.9 #the rate at which the AI agent should learn

dic = {}
#run through 1000 training episodes

for episode in range(10000):
    #refresh field
    field = np.full((environmentRows, environmentColumns), 1)
    fieldAgent = Field(field, environmentRows, environmentColumns)
    field = fieldAgent.createObstacles(indicesToChange)

    #refresh agents
    container = Container(field)
    tractor = Tractor(container, field)
    harvesterAgent = Harvester(field, q_values)
    fieldAgent = Field(field, environmentRows, environmentColumns)

    #get the starting location for this episode
    row_index, column_index = 1, 1
    episodeDic = {}

    #continue taking actions (i.e., moving) until we reach a terminal state
    #(i.e., until we reach the item packaging area or crash into an item storage location)
    cont = 0
    success = False
    while not fieldAgent.is_terminal_state(row_index, column_index) :
        #choose which action to take (i.e., where to move next)
        action_index = harvesterAgent.get_next_action(row_index, column_index, epsilon)

        #perform the chosen action, and transition to the next state (i.e., move to the next location)
        old_row_index, old_column_index = row_index, column_index #store the old row and column indexes
        row_index, column_index = harvesterAgent.get_next_location(row_index, column_index, action_index)
        tractor.move([row_index, column_index])

        #receive the reward for moving to the new state, and calculate the temporal difference
        reward = field[row_index, column_index]
    
        if reward == 1: 
            harvesterAgent.harvest()
            tractor.loadContainer(1)
        if fieldAgent.isEmpty(): 
            reward = 100
            success = True

        old_q_value = q_values[old_row_index, old_column_index, action_index]
        temporal_difference = reward + (discount_factor * np.max(q_values[row_index, column_index])) - old_q_value

        #update the Q-value for the previous state and action pair
        new_q_value = old_q_value + (learning_rate * temporal_difference)
        q_values[old_row_index, old_column_index, action_index] = new_q_value
        cont += 1

        episodeDic[f"step{cont}"] = {
                    "harvesterPosition": harvesterAgent.position,
                    "tractorPosition": tractor.position,
                    "containerPosition": tractor.container.position,
                    "containerLoad": tractor.container.load,
                    "field": [row[:] for row in field.tolist()],
                }
        
    dic[f"episode{episode}"] = {
        "steps": episodeDic,
        "success": success
        }
print('Training complete!')

with open("100reward1000episodesFieldEncapsulated.json", "w") as outfile: 
    json.dump(dic, outfile)
