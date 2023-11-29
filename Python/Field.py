import random
import agentpy as ap


class Field(ap.Agent):
    def __init__(self, field, environmentRows, environmentColumns):
        self.field = field
        self.environmentRows = environmentRows
        self.environmentColumns = environmentColumns
   
    #define a function that determines if the specified location is a terminal state
    def is_terminal_state(self, current_row_index, current_column_index):
        #if the reward for this location is -1, then it is not a terminal state (i.e., it is a 'white square')
        if self.isEmpty(): return True
        
        if (self.field[current_row_index, current_column_index] == -1 or self.field[current_row_index, current_column_index] == 1): return False
        
        return True

    def getIndicesToChange(self, amountOfObstacles):
        indices_to_change = set()
        while len(indices_to_change) < amountOfObstacles:
            row = random.randint(0, self.environmentRows - 1)
            col = random.randint(0, self.environmentColumns - 1)
            indices_to_change.add((row, col))
        return indices_to_change

    def createObstacles(self, indices_to_change):
        # Change the values at the selected indices to -100
        for row, col in indices_to_change:
            self.field[row][col] = -100

        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if i == 0 or i == len(self.field) - 1 or j == 0 or j == len(self.field[i]) - 1:
                    self.field[i][j] = -100
        return self.field


    def isEmpty(self):
        for row in self.field:
            for element in row:
                if element == 1: return False
        
        return True