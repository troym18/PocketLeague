from player import Player
import math

DT = 1 / 60

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def normalize(vector):
    magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
    if magnitude == 0:
        return [0, 0]
    return [vector[0] / magnitude, vector[1] / magnitude]

class Ball:
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.r = 30
        self.damping = 0.7
        self.vx = 0
        self.vy = 0
    
    def updatePosition(self, app):
        gravity = 200
        # Update position based on velocity
        self.cx += self.vx * DT
        self.cy += self.vy * DT
        self.vy += gravity * DT

        self.handleWallCollision(app)

    def handleWallCollision(self, app):
        if self.cx - self.r < app.mapLeft or self.cx + self.r > app.mapRight:
            self.vx *= -self.damping 
            self.cx = max(self.cx, app.mapLeft + self.r)
            self.cx = min(self.cx, app.mapRight - self.r)

        if self.cy - self.r < app.mapTop or self.cy + self.r > app.mapBottom:
            self.vy *= -self.damping 
            self.cy = max(self.cy, app.mapTop + self.r)
            self.cy = min(self.cy, app.mapBottom - self.r)


    def handlePlayerCollision(self, player):
        nearestX = max(player.cx - player.width / 2, min(self.cx, player.cx + player.width / 2))
        nearestY = max(player.cy - player.height / 2, min(self.cy, player.cy + player.height / 2))

        if distance(self.cx, self.cy, nearestX, nearestY) < self.r:
            self.vx = 1.4 * player.vx
            self.vy = 1.4 * player.vy
