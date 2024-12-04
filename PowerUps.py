from cmu_graphics import *
import math
import time
class powerUp:
    def __init__(self, cx, cy, type):
        self.cx = cx
        self.cy = cy
        self.type = type
        self.radius = 15
        self.startTime = 0
        self.active = True
        self.appliedPlayer = None

    def draw(self):
        fill = 'black'
        if self.type == "speed":
            fill = 'red'
        elif self.type == "boost":
            fill = 'yellow'
        elif self.type == "swap":
            fill = 'green'
        self.cy = self.cy + 5 * math.sin(time.time())
        drawCircle(self.cx, self.cy, self.radius, fill = fill)

    def apply(self, player, otherPlayer):
        if self.type == "speed":
            player.speed *= 1.5
        elif self.type == "boost":
            player.boostLevel = 100
        elif self.type == "swap":
            tempx = player.cx
            tempy = player.cy
            player.cx, player.cy = otherPlayer.cx, otherPlayer.cy
            otherPlayer.cx, otherPlayer.cy = tempx, tempy
        self.startTime = time.time()
    
    def revert(self, player):
        if self.type == "speed":
            player.speed /= 1.5