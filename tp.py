from cmu_graphics import *
from player import Player

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.stepsPerSecond=60
    app.mapTop=75
    app.mapLeft=25
    app.cornerRadius=100
    app.mapRight=1175
    app.mapBottom=725
    app.players=[Player(100,app.mapBottom-50,0,'blue',app)]

def redrawAll(app):
    drawMap(app)
    drawPlayers(app)

def drawMap(app):
    border='black'
    borderWidth=5

    #Map edges
    drawLine(app.mapLeft + app.cornerRadius, app.mapTop, app.mapRight - app.cornerRadius, app.mapTop, fill=border, lineWidth=borderWidth)
    drawLine(app.mapLeft + app.cornerRadius, app.mapBottom, app.mapRight - app.cornerRadius, app.mapBottom, fill=border, lineWidth=borderWidth)
    drawLine(app.mapLeft, app.mapTop + app.cornerRadius, app.mapLeft, app.mapBottom - app.cornerRadius, fill=border, lineWidth=borderWidth)
    drawLine(app.mapRight, app.mapTop + app.cornerRadius, app.mapRight, app.mapBottom - app.cornerRadius, fill=border, lineWidth=borderWidth)

    #Rounded Corners
    drawArc(app.mapLeft + app.cornerRadius, app.mapTop + app.cornerRadius, app.cornerRadius*2+4, app.cornerRadius*2+4, 
            90, 90, fill=None, border=border, borderWidth=borderWidth)
    drawArc(app.mapRight - app.cornerRadius, app.mapTop + app.cornerRadius, app.cornerRadius*2+4, app.cornerRadius*2+4, 
            0, 90, fill=None, border=border, borderWidth=borderWidth)
    drawArc(app.mapRight - app.cornerRadius, app.mapBottom - app.cornerRadius, app.cornerRadius*2+4, app.cornerRadius*2+4, 
            270, 90, fill=None, border=border, borderWidth=borderWidth)
    drawArc(app.mapLeft + app.cornerRadius, app.mapBottom - app.cornerRadius, app.cornerRadius*2+4, app.cornerRadius*2+4, 
            180, 90, fill=None, border=border, borderWidth=borderWidth)
    
    #Fill in corners
    drawCircle(app.mapLeft + app.cornerRadius, app.mapTop + app.cornerRadius, app.cornerRadius-3, fill='white')
    drawCircle(app.mapRight - app.cornerRadius, app.mapTop + app.cornerRadius, app.cornerRadius-3, fill='white')
    drawCircle(app.mapRight - app.cornerRadius, app.mapBottom - app.cornerRadius, app.cornerRadius-3, fill='white')
    drawCircle(app.mapLeft + app.cornerRadius, app.mapBottom - app.cornerRadius, app.cornerRadius-3, fill='white')

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
        drawRect(player.cx,player.cy,50,20,fill=player.team,rotateAngle=player.dir)

def onStep(app):
    for player in app.players:
        player.checkAirborne(app)
        player.updateMovement(app)
        
def onKeyHold(app,key):
    myPlayer=app.players[0]
    if key == 'd' and not myPlayer.inAir:
        myPlayer.increaseSpeed(10)
    if key == 'a' and not myPlayer.inAir:
        myPlayer.increaseSpeed(-10)
    if key == 'w' and myPlayer.inAir:
        myPlayer.rotate(10)
    if key == 's' and myPlayer.inAir:
        myPlayer.rotate(-10)
    if key=='space' and not myPlayer.inAir:
        myPlayer.vy+=100
    
runApp()