import math
import time

DT = 1 / 60
CONVERSION = math.pi/180

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
        self.speed = 250
        self.height = 20
        self.width = 50
        self.numJumps = 0
        self.firstJumpTime = 0
        self.secondJumpTime = 0
        self.touchingBLCircle = False
        self.touchingBRCircle = False
        self.touchingTLCircle = False
        self.touchingTRCircle = False

    def moveLeft(self):
        self.vx = self.speed * -math.cos(self.dir * CONVERSION)
        self.vy = self.speed * math.sin(self.dir * CONVERSION)

    def moveRight(self):
        self.vx = self.speed * math.cos(self.dir * CONVERSION)
        self.vy = self.speed * -math.sin(self.dir * CONVERSION)

    def decelerate(self):
        if abs(self.vx) > 20 or abs(self.vy) > 20:
            self.vx *= 0.5
            self.vy *= 0.5
        else:
            self.vx, self.vy = 0, 0
        return

    def jump(self):
        jumpStrength = 300
        normal = 90 - self.dir
        self.vy -= jumpStrength * math.sin(normal * CONVERSION)
        self.vx += jumpStrength * math.cos(normal * CONVERSION)
        self.inAir = True

    def rotate(self, angle):
        self.dir += angle

    def checkAirborne(self):
        tolerance = 5
        
        isGrounded = (
            abs(self.cy - (self.app.mapBottom - self.height / 2)) <= tolerance
            and self.vy >= 0
        )
        touchingLeftWall = (
            abs(self.cx - (self.app.mapLeft + self.width / 2)) <= tolerance
            and self.vx < 0
        )
        touchingRightWall = (
            abs(self.cx - (self.app.mapRight - self.width / 2)) <= tolerance
            and self.vx > 0
        )
        touchingCeiling = (
            abs(self.cy - (self.app.mapTop + self.height / 2)) <= tolerance
            and self.vy < 0
        )
        self.touchingBLCircle=(
            distance (self.cx, self.cy, self.app.BLCircle[0], self.app.BLCircle[1]) >= self.app.cornerRadius 
                    and self.cx < self.app.BLCircle[0] and self.cy > self.app.BLCircle[1]
        )
        self.touchingBRCircle=(
            distance (self.cx, self.cy, self.app.BRCircle[0], self.app.BRCircle[1]) >= self.app.cornerRadius 
                    and self.cx > self.app.BRCircle[0] and self.cy > self.app.BRCircle[1]
        )
        self.touchingTLCircle=(
            distance (self.cx, self.cy, self.app.TLCircle[0], self.app.TLCircle[1]) >= self.app.cornerRadius 
                    and self.cx < self.app.TLCircle[0] and self.cy < self.app.TLCircle[1]
        )
        self.touchingTRCircle=(
            distance (self.cx, self.cy, self.app.TRCircle[0], self.app.TRCircle[1]) >= self.app.cornerRadius 
                    and self.cx > self.app.TRCircle[0] and self.cy < self.app.TRCircle[1]
        )
        self.inAir = not (isGrounded or touchingLeftWall or touchingRightWall or touchingCeiling 
                        or self.touchingBLCircle or self.touchingBRCircle or
                        self.touchingTLCircle or self.touchingTRCircle)

    
    def updateMovement(self):
        gravity = 200
        if self.inAir:
            self.vy += gravity * DT
        else:
            if abs(self.vy) < 20:
                self.vy = 0
            if abs(self.vx) < 20:
                self.vx = 0
        
        self.cx += self.vx * DT
        self.cy += self.vy * DT

        self.checkBoundary()

    def checkBoundary(self):
        # Check each corner circle for boundary violations
        if (self.touchingBLCircle or self.touchingBRCircle or
            self.touchingTLCircle or self.touchingTRCircle):

            angleToCenter = math.atan2(self.cy - self.app.BLCircle[1], self.cx - self.app.BLCircle[0]) * 1/CONVERSION
            self.dir = angleToCenter - 90
            self.cx = self.app.BLCircle[0] + self.app.cornerRadius * math.cos(angleToCenter * CONVERSION)
            self.cy = self.app.BLCircle[1] + self.app.cornerRadius * math.sin(angleToCenter * CONVERSION)
        
        else:
            # Handle rectangle boundaries (edges of the map outside corner circles)
            self.cx = max(self.app.mapLeft + self.width / 2, 
                            min(self.cx, self.app.mapRight - self.width / 2))
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