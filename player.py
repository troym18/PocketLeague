import math

DT = 1 / 60

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def normalize(vector):
    magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
    if magnitude == 0:
        return [0, 0]
    return [vector[0] / magnitude, vector[1] / magnitude]

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
        # Vector normal to surface player is on
        self.normal = [0, 1]  # Default normal pointing upward

    def moveLeft(self):
        if not self.inAir:
            # Move left along the surface's tangent direction
            tangent = [-self.normal[1], self.normal[0]]  # Perpendicular to normal
            self.vx = tangent[0] * -self.speed
            self.vy = tangent[1] * -self.speed

    def moveRight(self):
        if not self.inAir:
            # Move right along the surface's tangent direction
            tangent = [self.normal[1], -self.normal[0]]  # Perpendicular to normal
            self.vx = tangent[0] * self.speed
            self.vy = tangent[1] * self.speed

    def decelerate(self):
        # Gradually reduce velocity components when grounded
        if abs(self.vx) > 50 or abs(self.vy) > 50:
            decelerationFactor = normalize([self.vx, self.vy])
            self.vx -= decelerationFactor[0] * 50
            self.vy -= decelerationFactor[1] * 50
        else:
            self.vx, self.vy = 0, 0

    def jump(self):
        # Jump in the direction of the normal vector
        jumpStrength = 200
        normalizedNormal = normalize(self.normal)
        self.vx += normalizedNormal[0] * jumpStrength
        self.vy += normalizedNormal[1] * jumpStrength

    def rotate(self, angle):
        # Rotate player orientation based on angle (for aerial control)
        self.dir += angle

    def checkAirborne(self):
        # Check if player is airborne by comparing distance to ground or surface
        grounded = False

        # Check flat boundaries (floor/ceiling/walls)
        if abs(self.cy - self.app.mapBottom) <= (self.height / 2 + 1):  # Floor check
            grounded = True
            self.normal = [0, 1]
        
        elif abs(self.cy - self.app.mapTop) <= (self.height / 2 + 1):  # Ceiling check
            grounded = True
            self.normal = [0, -1]
        
        elif abs(self.cx - self.app.mapLeft) <= (self.width / 2 + 1):  # Left wall check
            grounded = True
            self.normal = [1, 0]
        
        elif abs(self.cx - self.app.mapRight) <= (self.width / 2 + 1):  # Right wall check
            grounded = True
            self.normal = [-1, 0]

        # Check circular boundaries (corners)
        for circle in [self.app.TLCircle, 
                       self.app.TRCircle,
                       self.app.BLCircle,
                       self.app.BRCircle]:
            
            distanceToCircleCenter = distance(self.cx, 
                                              self.cy,
                                              circle[0],
                                              circle[1])
            
            if distanceToCircleCenter <= (self.app.cornerRadius + (self.height / 2)):
                angleToCenter = math.atan2(self.cy - circle[1], circle[0] - self.cx)
                outwardNormalX = math.cos(angleToCenter)
                outwardNormalY = math.sin(angleToCenter)
                self.normal = normalize([outwardNormalX, outwardNormalY])
                grounded = True

        # Update airborne status based on checks above
        self.inAir = not grounded

    def updateMovement(self):
        gravityStrength = 200

        if not self.inAir:
            # Align player direction with surface normal when grounded
            normalizedNormal = normalize(self.normal)
            angleToNormal = math.atan2(normalizedNormal[1], normalizedNormal[0])
            self.dir = math.degrees(angleToNormal)
        
        else:
            # Apply gravity in world space when airborne
            gravityVector = [0, gravityStrength]
            normalizedGravityVector = normalize(gravityVector)
            self.vx += normalizedGravityVector[0] * DT * gravityStrength
            self.vy += normalizedGravityVector[1] * DT * gravityStrength
        
        # Update position based on velocity and time step
        self.cx += self.vx * DT
        self.cy += self.vy * DT

        # Check boundaries and adjust position accordingly after movement
        self.checkBoundary()

    def checkBoundary(self):
        for circle in [self.app.TLCircle,
                       self.app.TRCircle,
                       self.app.BLCircle,
                       self.app.BRCircle]:
            
            distanceToCircleCenter = distance(self.cx,
                                              self.cy,
                                              circle[0],
                                              circle[1])
            
            if distanceToCircleCenter <= (self.app.cornerRadius + (self.height / 2)):
                angleToCenter = math.atan2(self.cy - circle[1], circle[0] - self.cx)
                edgeX = circle[0] + math.cos(angleToCenter) * (self.app.cornerRadius)
                edgeY = circle[1] + math.sin(angleToCenter) * (self.app.cornerRadius)

                outwardNormalX = edgeX - circle[0]
                outwardNormalY = edgeY - circle[1]
                outwardNormalVector = normalize([outwardNormalX, outwardNormalY])

                # Snap player to edge of circle and update normal vector.
                self.cx, self.cy = edgeX, edgeY
                self.normal= outwardNormalVector
