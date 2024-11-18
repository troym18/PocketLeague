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
        self.playerHeight = 20
        #Vector normal to surface player is on
        self.normal=(1,0)

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
        if abs(self.cy - self.app.mapBottom) <= self.playerHeight/2 + 1 :
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
        
        self.cx = max(self.app.mapLeft, min(self.cx, self.app.mapRight))
        self.cy = max(self.app.mapTop, 
                  min(self.cy, self.app.mapBottom - self.playerHeight/2))

    def __repr__(self):
        return f'''Car is on team {self.team} at position: {self.cx}, 
                 {self.cy} in direction {self.dir}'''