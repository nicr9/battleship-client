import numpy as np

class StateSpace(object):
    def __init__(self, x, y):
        self.state = np.zeros([y,x])

    def mark(self, x, y):
        self.state[y, x] = 1

    def mark_rect(self, x_min, x_max, y_min, y_max):
        self.state[y_min:(y_max + 1), x_min:(x_max + 1)] = 1

    def next_coords(self):
        for y in self.state.shape[0]:
            for x in self.state.shape[1]:
                if self.state[y, x] == 0:
                    return x, y

