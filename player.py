import numpy as np

DT = 1/60

def vec(x, y):
    return np.array([x, y])

def distance(x1 ,y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

class Player:
    def __init__(self, pos, direction, team):
        #Vectors
        self.pos = pos
        self.vel = vec(0,0)
        self.accel = vec(0,0)
        
        self.dir = direction
        self.team = team
        self.inAir = False
    
    def increaseSpeed(self, accelX):
        if self.vel < 100:
            self.accel[0] = accelX
    
    def rotate(self, angle):
        self.dir += angle

    # def updateMovemnt(self):
    #     if self.inAir:
    #         self.accel[1] = -100
    #     else:
    #         self.accel[1] = 0
    #         #Friction
    #         self.vel = self.vel * (9/10) 
    #     self.vel += self.accel * DT
    #     self.pos += self.vel * DT
    
    def checkAirborne(self, app):
    # Check if the player is within the map bounds
        if (self.pos[0] < app.mapLeft or self.pos[0] > app.mapRight or
            self.pos[1] < app.mapTop or self.pos[1] > app.mapBottom):
            self.inAir = True
        else:
            # Check if the player is close to the ground (bottom of the map)
            ground_threshold = 5  # Adjust this value as needed
            if self.pos[1] >= app.mapBottom - ground_threshold:
                self.inAir = False
            else:
                self.inAir = True

    def updateMovement(self):
        if self.inAir:
            self.accel[1] = -100  # Gravity
        else:
            self.accel[1] = 0
            # Friction
            self.vel = self.vel * (9/10)
        
        self.vel += self.accel * DT
        self.pos += self.vel * DT
        
        # Constrain player position within map bounds
        self.pos[0] = max(app.mapLeft, min(self.pos[0], app.mapRight))
        self.pos[1] = max(app.mapTop, min(self.pos[1], app.mapBottom))

        

    def __repr__(self):
        return f'Car is on team{team} at position:{self.pos[0]},{self.pos[1]} in direction {self.dir}'
    