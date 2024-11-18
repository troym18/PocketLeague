DT = 1/60


def distance(x1 ,y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

class Player:
    def __init__(self, cx, cy , direction, team, app):

        self.app = app
        self.cx = cx
        self.cy = cy
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

        
        self.dir = direction
        self.team = team
        self.inAir = False
    
    def increaseSpeed(self, accelX):
        if self.vel < 100:
            self.ax = accelX
    
    def rotate(self, angle):
        self.dir += angle
    
    def checkAirborne(self, app):
    # Check if the player is within the map bounds
        if (self.cx < self.app.mapLeft or self.cx > self.app.mapRight or
            self.cy < self.app.mapTop or self.cy > self.app.mapBottom):
            self.inAir = True
        else:
            # Check if the player is close to the ground (bottom of the map)
            if self.cy >= self.app.mapBottom - 20:
                self.inAir = False
            else:
                self.inAir = True

    def updateMovement(self, app):
        if self.inAir:
            self.ay = 150  # Gravity
        else:
            self.ay = 0
            # Friction
            self.cx = self.cx * (9/10)
        
        self.vx += self.ax * DT
        self.vy += self.ay * DT
        self.cx += self.vx * DT
        self.cy += self.vy * DT
        
        # Constrain player position within map bounds
        self.cx = max(self.app.mapLeft, min(self.cx, self.app.mapRight))
        self.cy = max(self.app.mapTop, min(self.cy, self.app.mapBottom))

        

    def __repr__(self):
        return f'Car is on team{team} at position:{self.cx},{self.cy} in direction {self.dir}'
    