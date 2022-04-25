import numpy as np

class SimpleReflexAgent:

    def create_q_table(self):
        q_table = np.zeros((len(self.states), (len(self.actions))))
        # Put your source code here
        # w.g. q_table[0, 1] = 5 asserts a q_value of 5 to perform action 1 in state 0
        # the corresponding states and actions can be obtained by self.states[0] and
        # self.actions[1] in this example
        return q_table




