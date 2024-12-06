from player import Player
import math
import random
import time

DT = 1 / 60

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def normalize(vector):
    magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
    if magnitude == 0:
        return [0, 0]
    return [vector[0] / magnitude, vector[1] / magnitude]

class Ball:
    def __init__(self, cx, cy, app):
        self.cx = cx
        self.cy = cy
        self.r = 30
        self.damping = 0.7
        self.vx = 0
        self.vy = 0
        self.app = app
    
    def updatePosition(self, app):
        self.cx += self.vx * DT
        self.cy += self.vy * DT
        self.vy += self.app.gravity * DT

        self.handleWallCollision(app)

    def handleWallCollision(self, app):
        touchingBLCircle=(
        distance (self.cx, self.cy, self.app.BLCircle[0], 
        self.app.BLCircle[1]) >= self.app.cornerRadius - self.r 
        and self.cx < self.app.BLCircle[0] and self.cy > self.app.BLCircle[1]
        )
        touchingBRCircle=(
        distance (self.cx, self.cy, self.app.BRCircle[0], 
        self.app.BRCircle[1]) >= self.app.cornerRadius - self.r 
        and self.cx > self.app.BRCircle[0] and self.cy > self.app.BRCircle[1]
        )
        touchingTLCircle=(
        distance (self.cx, self.cy, self.app.TLCircle[0], 
        self.app.TLCircle[1]) >= self.app.cornerRadius - self.r 
        and self.cx < self.app.TLCircle[0] and self.cy < self.app.TLCircle[1]
        )
        touchingTRCircle=(
        distance (self.cx, self.cy, self.app.TRCircle[0], 
        self.app.TRCircle[1]) >= self.app.cornerRadius - self.r 
        and self.cx > self.app.TRCircle[0] and self.cy < self.app.TRCircle[1]
        )
        if touchingBLCircle:
            self.cx = self.app.BLCircle[0]
            self.cy = self.app.BLCircle[1]
            self.vx = random.randrange(100, 400)
            self.vy = random.randrange(-400, -100)
        
        if touchingBRCircle:
            self.cx = self.app.BRCircle[0]
            self.cy = self.app.BRCircle[1]
            self.vx = random.randrange(-400, -100)
            self.vy = random.randrange(-400, -100)
        
        if touchingTLCircle:
            self.cx = self.app.TLCircle[0]
            self.cy = self.app.TLCircle[1]
            self.vx = random.randrange(100, 400)
            self.vy = random.randrange(100, 400)
        
        if touchingTRCircle:
            self.cx = self.app.TRCircle[0]
            self.cy = self.app.TRCircle[1]
            self.vx = random.randrange(-400, -100)
            self.vy = random.randrange(100, 400)
            
        elif self.cx - self.r < app.mapLeft or self.cx + self.r > app.mapRight:
            self.vx *= -self.damping 
            self.cx = max(self.cx, app.mapLeft + self.r)
            self.cx = min(self.cx, app.mapRight - self.r)

        elif self.cy - self.r < app.mapTop or self.cy + self.r > app.mapBottom:
            self.vy *= -self.damping 
            self.cy = max(self.cy, app.mapTop + self.r)
            self.cy = min(self.cy, app.mapBottom - self.r)


    def handlePlayerCollision(self, player):
        nearestX = max(player.cx - player.width / 2, 
        min(self.cx, player.cx + player.width / 2))
        nearestY = max(player.cy - player.height / 2, 
        min(self.cy, player.cy + player.height / 2))
        if distance(self.cx, self.cy, nearestX, nearestY) < self.r:
            if player.vx == 0 and player.vy == 0:
                self.vx = 0.7 * -self.vx
                self.vy = 0.7 * -self.vy
            elif player.vx != 0 and player.vy == 0:
                self.vx = 1.4 * player.vx
                self.vy = 0.7 * -self.vy
            elif player.vx == 0 and player.vy != 0:
                self.vx = 0.7 * -self.vx
                self.vy = 1.4 * player.vy
            else:
                self.vx = 1.4 * player.vx
                self.vy = 1.4 * player.vy