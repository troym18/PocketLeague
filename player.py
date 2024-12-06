import math
import time
import random

DT = 1 / 60

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

class Player:
    def __init__(self, centerX, centerY, direction, team, app):
        self.app = app
        self.cx = centerX
        self.cy = centerY
        self.vx = 0
        self.vy = 0
        self.dir = direction
        self.team = team
        self.inAir = False
        self.speed = 100
        self.height = 30
        self.width = 75
        self.numJumps = 0
        self.firstJumpTime = 0
        self.secondJumpTime = 0
        self.boostLevel = 33
        self.isBoosting = False
        self.boostCooldown = 0
        self.inverted = False
        self.touchingLeftWall = False
        self.touchingRightWall = False

    def moveLeft(self):
        if not self.inAir and abs(self.vx) < self.speed * 5:
            self.vx += self.speed * -math.cos(math.radians(self.dir))
        if not self.inAir and abs(self.vy) < self.speed * 5:
            self.vy += self.speed * math.sin(math.radians(self.dir))
        if self.touchingLeftWall or self.touchingRightWall:
            self.inverted = False
        else:
            self.inverted = True


    def moveRight(self):
        if not self.inAir and abs(self.vx) < self.speed * 5:
            self.vx += self.speed * math.cos(math.radians(self.dir))
        if not self.inAir and abs(self.vy) < self.speed * 5:
            self.vy += self.speed * -math.sin(math.radians(self.dir))
        if self.touchingLeftWall or self.touchingRightWall:
            self.inverted = True
        else:
            self.inverted = False

    def decelerate(self):
        if abs(self.vx) > 20 or abs(self.vy) > 20:
            self.vx *= 0.5
            self.vy *= 0.5
        else:
            self.vx, self.vy = 0, 0
        return

    def boost(self):
        if self.inAir and self.inverted:
            self.vx += 5 * math.cos(math.radians(self.dir - 180))
            self.vy += 5 * math.sin(math.radians(self.dir - 180))
        elif self.inAir and not self.inverted:
            self.vx += 5 * math.cos(math.radians(self.dir))
            self.vy += 5 * math.sin(math.radians(self.dir))
        else:
            self.vx *= 1.25
            self.vy *= 1.25
        self.boostLevel -= 1
    
    def updateBoostState(self):
        currentTime = time.time()
        if (currentTime - self.boostCooldown >= 1 and 
        not self.isBoosting and self.boostLevel < 100):
            self.boostLevel += 1
    
    def jump(self):
        jumpStrength = 200
        normal = 90 - self.dir
        self.vy -= jumpStrength * math.sin(math.radians(normal))
        self.vx += jumpStrength * math.cos(math.radians(normal))

    def rotate(self, angle):
        self.dir += angle

    def checkAirborne(self):
        tolerance = 5
        
        isGrounded = (
            abs(self.cy - (self.app.mapBottom - self.height / 2)) <= tolerance
            and self.vy >= 0
        )
        self.touchingLeftWall = (
            abs(self.cx - (self.app.mapLeft + self.height / 2)) <= tolerance
        )
        self.touchingRightWall = (
            abs(self.cx - (self.app.mapRight - self.height / 2)) <= tolerance
        )
        touchingCeiling = (
            abs(self.cy - (self.app.mapTop + self.height / 2)) <= tolerance
        )
        self.inAir = not (isGrounded or self.touchingLeftWall 
                        or self.touchingRightWall or touchingCeiling)
        if not self.inAir:
            self.numJumps = 2

    
    def updateMovement(self):
        if self.inAir:
            self.vy += self.app.gravity * DT
        else:
            if abs(self.vy) < 20:
                self.vy = 0
            if abs(self.vx) < 20:
                self.vx = 0
        
        self.cx += self.vx * DT
        self.cy += self.vy * DT

        self.checkBoundary()

    def checkBoundary(self):
        touchingBLCircle=(
            distance (self.cx, self.cy, self.app.BLCircle[0], 
                      self.app.BLCircle[1]) >= self.app.cornerRadius 
                      and self.cx < self.app.BLCircle[0] 
                      and self.cy > self.app.BLCircle[1]
        )
        touchingBRCircle=(
            distance (self.cx, self.cy, self.app.BRCircle[0], 
                      self.app.BRCircle[1]) >= self.app.cornerRadius 
                      and self.cx > self.app.BRCircle[0] 
                      and self.cy > self.app.BRCircle[1]
        )
        touchingTLCircle=(
            distance (self.cx, self.cy, self.app.TLCircle[0], 
                      self.app.TLCircle[1]) >= self.app.cornerRadius 
                      and self.cx < self.app.TLCircle[0] 
                      and self.cy < self.app.TLCircle[1]
        )
        touchingTRCircle=(
            distance (self.cx, self.cy, self.app.TRCircle[0], 
                      self.app.TRCircle[1]) >= self.app.cornerRadius 
                      and self.cx > self.app.TRCircle[0] 
                      and self.cy < self.app.TRCircle[1]
        )
        if touchingBLCircle:
            self.vx = random.randrange(250, 350)
            self.vy = random.randrange(-350, -250)
            self.inAir = True
            self.numJumps = 1
        
        if touchingBRCircle:
            self.vx = random.randrange(-350, -250)
            self.vy = random.randrange(-350, -250)
            self.inAir = True
            self.numJumps = 1
        
        if touchingTLCircle:
            self.vx = random.randrange(250, 350)
            self.vy = random.randrange(250, 350)
            self.inAir = True
            self.numJumps = 1
        
        if touchingTRCircle:
            self.vx = random.randrange(-350, -250)
            self.vy = random.randrange(250, 350)
            self.inAir = True
            self.numJumps = 1
        
        else:
            # Handle rectangle boundaries
            self.cx = max(self.app.mapLeft + self.height / 2, 
                            min(self.cx, self.app.mapRight - self.height / 2))
            self.cy = max(self.app.mapTop + self.height / 2, 
                            min(self.cy, self.app.mapBottom - self.height / 2))
            if abs(self.cx - self.app.mapLeft) < self.width + 2:
                self.dir = 90
            if abs(self.cx - self.app.mapRight) < self.width + 2:
                self.dir = 270
            if abs(self.cy - self.app.mapTop) < self.height + 2:
                self.dir = 180
            if abs(self.cy - self.app.mapBottom) < self.height + 2:
                self.dir = 0


    def __repr__(self):
        return f'''Car is on team {self.team} at position: {self.cx}, 
                 {self.cy} in direction {self.dir}'''