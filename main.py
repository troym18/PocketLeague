from cmu_graphics import *
from player import Player
from ball import Ball
import time
import math
DT = 1 / 60
CONVERSION = math.pi / 180

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.stepsPerSecond=60
    app.mapTop=75
    app.mapLeft=25
    app.cornerRadius=100
    app.mapRight=1175
    app.mapBottom=725
    app.players=[Player(200,app.mapBottom-50,0,'blue',app)]
    app.TRCircle = [app.mapRight - app.cornerRadius, app.mapTop + app.cornerRadius]
    app.TLCircle = [app.mapLeft + app.cornerRadius, app.mapTop + app.cornerRadius]
    app.BLCircle = [app.mapLeft + app.cornerRadius, app.mapBottom - app.cornerRadius]
    app.BRCircle = [app.mapRight - app.cornerRadius, app.mapBottom - app.cornerRadius]
    app.circles = [app.TRCircle, app.TLCircle, app.BLCircle, app.BRCircle]
    app.ball = Ball(app.width//2, app.height//2, )

def redrawAll_start(app):

def redrawAll(app):
    drawMap(app)
    drawPlayers(app)
    drawBall(app)

def drawBall(app):
    drawCircle(app.ball.cx, app.ball.cy, app.ball.r, fill='grey')

def drawMap(app):
    border='black'
    borderWidth=5

    #Map edges
    drawLine(app.TLCircle[0], app.mapTop, 
             app.TRCircle[0], app.mapTop, 
             fill=border, lineWidth=borderWidth)
    drawLine(app.BLCircle[0], app.mapBottom, 
             app.BRCircle[0], app.mapBottom, 
             fill=border, lineWidth=borderWidth)

    drawLine(app.mapLeft, app.TLCircle[1], 
             app.mapLeft, app.BLCircle[1], 
             fill=border, lineWidth=borderWidth)
             
    drawLine(app.mapRight, app.TRCircle[1], 
             app.mapRight, app.BRCircle[1], 
             fill=border, lineWidth=borderWidth)

    #Rounded Corners
    sweepAngle=90
    startAngle=0
    for circle in app.circles:
        drawArc(circle[0], circle[1], app.cornerRadius*2+4, 
                app.cornerRadius*2+4, startAngle, sweepAngle, 
                fill=None, border=border, borderWidth=borderWidth)
        startAngle+=90
    
    #Fill in corners
    for circle in app.circles:
        drawCircle(circle[0], circle[1], 
                   app.cornerRadius-3, fill='white')

    #Blue and Orange goals
    topGoalY=app.height/2+100
    bottomGoalY=app.height/2-100
    drawLine(25, topGoalY, 25, bottomGoalY, fill='blue', lineWidth=15)
    drawLine(app.width-25, topGoalY, app.width-25, bottomGoalY, 
            fill='orange', lineWidth=15)

    #Midfield point
    drawLine(app.width/2-10, app.height-75, app.width/2+10, app.height-75, 
            fill='red',lineWidth=10)

def drawPlayers(app):
    for player in app.players:
        fill = gradient(player.team,'black',start='top')
        drawRect(player.cx-player.width/2,player.cy-player.height/2,player.width,
                 player.height,fill=fill,rotateAngle=player.dir)
        normal = 90 - player.dir
        drawLine(player.cx, player.cy,player.cx + 50 * math.cos(normal * CONVERSION), 
                player.cy - 50 * math.sin(normal * CONVERSION))
         
def onKeyHold(app, keys):
    myPlayer = app.players[0]
    if 'd' in keys and not myPlayer.inAir:
        myPlayer.moveRight()
    elif 'a' in keys and not myPlayer.inAir:
        myPlayer.moveLeft()
    if 'w' in keys and myPlayer.inAir:
        myPlayer.rotate(5)
    if 's' in keys and myPlayer.inAir:
        myPlayer.rotate(-5)
    if 'space' in keys:
        if not myPlayer.inAir:
            myPlayer.jump() 
            myPlayer.firstJumpTime = time.time()
            myPlayer.numJumps = 1
        elif myPlayer.numJumps == 1:
            currentTime = time.time()
            if currentTime - myPlayer.firstJumpTime > 0.4:
                myPlayer.jump()
                myPlayer.numJumps -= 1

def onStep(app):
    app.ball.updatePosition(app)
    for player in app.players:
        player.checkAirborne()
        player.updateMovement()
        app.ball.handlePlayerCollision(player)
        if not player.inAir:
            player.decelerate()

def main():
    runAppWithScreens(initialScreen='start')

main()