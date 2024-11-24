import math
DT = 1/60


def distance(x1 ,y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

class Player:
    def __init__(self, cx, cy, direction, team, app):
        self.app = app
        self.cx = cx
        self.cy = cy
        self.vx = 0
        self.vy = 0
        self.dir = direction
        self.team = team
        self.inAir = False
        self.speed = 250
        self.height = 20
        self.width = 50
        #Vector normal to surface player is on
        self.normal=[0,1]

    def moveLeft(self):
        if not self.inAir:
            self.vx = -self.speed

    def moveRight(self):
        if not self.inAir:
            self.vx = self.speed

    def decelerate(self):
        if self.vx>50:
            self.vx -= 50
        elif self.vx<-50:
            self.vx += 50
        elif -50 <= self.vx <= 50:
            self.vx = 0

    def jump(self):
        self.vy = -200

    def rotate(self, angle):
        self.dir += angle

    def checkAirborne(self):
        if abs(self.cy - self.app.mapBottom) <= self.height/2 + 1 :
            self.inAir = False
        else:
            self.inAir = True

    def updateMovement(self):
        gravity = 200

        if self.inAir or self.vy < 0:
            self.vy += gravity * DT
            self.cy += self.vy * DT
        else:
            self.vy = 0
            self.dir=0

        self.cx += self.vx * DT

        self.checkBoundary()

    def checkBoundary(self):
        if (distance (self.cx, self.cy, self.app.BLCircle[0], self.app.BLCircle[1]) > self.app.cornerRadius 
        and self.cx < self.app.BLCircle[0] and self.cy > self.app.BLCircle[1]):
            #Put player center on point closest to circle
            # Calculate the angle between the player and the circle's center
            angle = math.atan2(self.cy - self.app.BLCircle[0], self.cx - self.app.BLCircle[1])
        
            # Place the player on the edge of the circle
            self.cx = self.app.BLCircle[0] + self.app.cornerRadius * math.cos(angle)
            self.cy = self.app.BLCircle[1] + self.app.cornerRadius * math.sin(angle)
        else:
            self.cx = max(self.app.mapLeft + self.width/2, 
                    min(self.cx, self.app.mapRight - self.width/2))
            self.cy = max(self.app.mapTop + self.height/2 , 
                    min(self.cy, self.app.mapBottom - self.height/2))

    def __repr__(self):
        return f'''Car is on team {self.team} at position: {self.cx}, 
                 {self.cy} in direction {self.dir}'''