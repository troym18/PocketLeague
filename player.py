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
        self.speed = 5  # Constant speed for left/right movement

    def moveLeft(self):
        if not self.inAir:
            self.vx = -self.speed

    def moveRight(self):
        if not self.inAir:
            self.vx = self.speed

    def stopHorizontalMovement(self):
        self.vx = 0

    def jump(self):
        if not self.inAir:
            self.vy = -15  # Adjust this value for desired jump height

    def rotate(self, angle):
        self.dir += angle

    def checkAirborne(self):
        ground_threshold = 20
        if self.cy >= self.app.mapBottom - ground_threshold:
            self.inAir = False
            self.cy = self.app.mapBottom - ground_threshold
            self.vy = 0
        else:
            self.inAir = True

    def updateMovement(self):
        gravity = 0.5  # Reduced gravity for smoother fall

        if self.inAir:
            self.vy += gravity
        else:
            self.vy = 0

        # Update position
        self.cx += self.vx
        self.cy += self.vy
        
        # Constrain player position within map bounds
        self.cx = max(self.app.mapLeft, min(self.cx, self.app.mapRight))
        self.cy = max(self.app.mapTop, min(self.cy, self.app.mapBottom))

    def __repr__(self):
        return f'Car is on team {self.team} at position: {self.cx}, {self.cy} in direction {self.dir}'