import numpy as np
def vec(x,y):
    return np.array([x, y])
class Player:
    def __init__(self, pos, vel, team):
        self.pos = pos
        self.vel = vel
        self.team = team