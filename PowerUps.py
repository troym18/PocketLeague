from cmu_graphics import *
import math
import time
class powerUp:
    def __init__(self, app, cx, cy, type):
        self.app = app
        self.cx = cx
        self.cy = cy
        self.type = type
        self.r = 15
        self.startTime = 0
        self.active = True
        self.appliedPlayer = None

    def draw(self):
        r = self.r
        y = self.cy
        fill = 'black'
        if self.type == "speed":
            fill = gradient('red', 'orange', start = 'center')
            y = self.cy + 5 * math.sin(4 * time.time())
        elif self.type == "boost":
            fill = gradient('yellow', 'white', start = 'center')
            y = self.cy + 5 * math.sin(4 * time.time())
        elif self.type == "swap":
            darkerGreen = rgb(0, 50, 0)
            fill = gradient('green', darkerGreen, start = 'center')
            y = self.cy + 5 * math.sin(4 * time.time())
        elif self.type == "gravity":
            fill = gradient('purple', 'indigo', start = 'center')
            r = self.r + 3 * math.sin( 4 * time.time())
        drawCircle(self.cx, y, r, fill = fill, border = 'black')

    def apply(self, player, otherPlayer):
        if self.type == "speed":
            player.speed *= 3
        elif self.type == "boost":
            player.boostLevel = 100
        elif self.type == "swap":
            tempx = player.cx
            tempy = player.cy
            player.cx, player.cy = otherPlayer.cx, otherPlayer.cy
            otherPlayer.cx, otherPlayer.cy = tempx, tempy
        elif self.type == "gravity":
            self.app.gravity *= -1
        self.startTime = time.time()

    
    def revert(self, player):
        if self.type == "speed":
            player.speed /= 3
        if self.type == "gravity":
            self.app.gravity *= -1