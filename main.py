from cmu_graphics import *
from player import Player
from ball import Ball
import time
import math

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    app.mapTop = 75
    app.mapLeft = 25
    app.cornerRadius = 100
    app.mapRight = 1175
    app.mapBottom = 725
    app.topGoalY = app.height/2 - 100
    app.bottomGoalY = app.height/2 + 100
    app.TRCircle = [app.mapRight - app.cornerRadius, app.mapTop + app.cornerRadius]
    app.TLCircle = [app.mapLeft + app.cornerRadius, app.mapTop + app.cornerRadius]
    app.BLCircle = [app.mapLeft + app.cornerRadius, app.mapBottom - app.cornerRadius]
    app.BRCircle = [app.mapRight - app.cornerRadius, app.mapBottom - app.cornerRadius]
    app.circles = [app.TRCircle, app.TLCircle, app.BLCircle, app.BRCircle]

#START

def start_redrawAll(app):
    buttonWidth = 300
    buttonHeight = 75
    drawLabel("Welcome to 112-League! ", app.width/2, 100, size=50, 
    font = 'monospace', fill = gradient('blue', 'orange', start='left'))
    drawRect(app.width/2 - buttonWidth/2, 200, buttonWidth, buttonHeight, 
            fill = None, border = 'black')
    drawLabel("Training Mode", app.width/2, 200 + buttonHeight/2, size = 30, 
              font = 'monospace')
    drawRect(app.width/2 - buttonWidth/2, 350, buttonWidth, buttonHeight, 
            fill = None, border = 'black')
    drawLabel("Multiplayer Mode", app.width/2, 350 + buttonHeight/2, size = 30, 
              font = 'monospace')
    drawRect(app.width/2 - buttonWidth/2, 500, buttonWidth, buttonHeight, 
            fill = None, border = 'black')
    drawLabel("How To Play", app.width/2, 500 + buttonHeight/2, size = 30, 
              font = 'monospace')

def start_onMousePress(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        200 <= mouseY <= 200 + buttonHeight):
        setActiveScreen('training')
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        350 <= mouseY <= 350 + buttonHeight):
        setActiveScreen('multiplayerStart')
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        500 <= mouseY <= 500 + buttonHeight):
        setActiveScreen('howTo')

#END START
#HOW TO PLAY

def howTo_redrawAll(app):
    drawLabel("Keys", app.width/2, 50, size = 50, font = 'monospace',
              fill = gradient('blue', 'orange', start='left'))
    drawLabel('Singleplayer',app.width/2, 100, 
             size= 30, font = 'monospace')
    drawLabel('w\t\t-\t\tRotate Car CounterClockwise',app.width/2, 150, 
             size= 25, font = 'monospace')
    drawLabel('s\t\t-\t\tRotate Car Clockwise',app.width/2, 200, 
             size= 25, font = 'monospace')
    drawLabel('d\t\t-\t\tDrive Forward',app.width/2, 250, 
             size= 25, font = 'monospace')
    drawLabel('a\t\t-\t\tDrive Backward',app.width/2, 300, 
             size= 25, font = 'monospace')
    drawLabel('space\t\t-\t\tJump',app.width/2, 350, 
             size= 25, font = 'monospace')
    drawLabel('e\t\t-\t\tBoost',app.width/2, 400, 
             size= 25, font = 'monospace')
    drawLabel('Multiplayer (Car 2)',app.width/2, 450, 
             size= 30, font = 'monospace')
    drawLabel('i\t\t-\t\tRotate Car CounterClockwise',app.width/2, 500, 
             size= 25, font = 'monospace')
    drawLabel('k\t\t-\t\tRotate Car Clockwise',app.width/2, 550, 
             size= 25, font = 'monospace')
    drawLabel('l\t\t-\t\tDrive Forward',app.width/2, 600, 
             size= 25, font = 'monospace')
    drawLabel('j\t\t-\t\tDrive Backward',app.width/2, 650, 
             size= 25, font = 'monospace')
    drawLabel('o\t\t-\t\tJump',app.width/2, 700, 
             size= 25, font = 'monospace')
    drawLabel('n\t\t-\t\tBoost',app.width/2, 750, 
             size= 25, font = 'monospace')
    drawLabel('Esc to return', 100, 50, size = 20, font = 'monospace')

def howTo_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

#END HOW TO PLAY
#MULTIPLAYER START

def multiplayerStart_redrawAll(app):
    buttonWidth = 300
    buttonHeight = 75
    drawLabel("Multiplayer Modes", app.width/2, 50, size = 50, 
            font = 'monospace', fill = gradient('blue', 'orange', start='left'))
    drawRect(app.width/2 - buttonWidth/2, 200, buttonWidth, buttonHeight, 
            fill = None, border = 'black')
    drawLabel("1v1 (Player)", app.width/2, 200 + buttonHeight/2, size = 30, 
              font = 'monospace')
    # drawRect(app.width/2 - buttonWidth/2, 350, buttonWidth, buttonHeight, 
    #         fill = None, border = 'black')
    # drawLabel("1v1 (AI)", app.width/2, 350 + buttonHeight/2, size = 30, 
    #           font = 'monospace')
    # drawRect(app.width/2 - buttonWidth/2, 500, buttonWidth, buttonHeight, 
    #         fill = None, border = 'black')
    # drawLabel("2v2 (AI)", app.width/2, 500 + buttonHeight/2, size = 30, 
    #           font = 'monospace')
    drawLabel('Esc to return', 100, 50, size = 20, font = 'monospace')

def multiplayerStart_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

def multiplayerStart_onMousePress(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        200 <= mouseY <= 200 + buttonHeight):
        setActiveScreen('oneVPlayer')
    # if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
    #     350 <= mouseY <= 350 + buttonHeight):
    #     setActiveScreen('1v1AI')
    # if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
    #     500 <= mouseY <= 500 + buttonHeight):
    #     setActiveScreen('2v2AI')

#END MULTIPLAYER START
#TRAINING MODE

def training_onScreenActivate(app):
    app.players =[Player(200, app.mapBottom - 10,0, 'gray', app)]
    app.ball = Ball(app.width//2, app.height//2, app)
    app.scored = False

def training_redrawAll(app):
    drawLabel("Training Mode", app.width/2, 20, size = 30, font = 'monospace')
    drawLabel('Esc to return', 100, 50, size = 20, font = 'monospace')
    drawMap(app)
    drawPlayers(app)
    drawBall(app)
    if app.scored:
        drawLabel('GOAL!', app.width/2, app.height/2, size = 50, 
        font = 'monospace', fill = gradient('orange','blue',start = 'left'))
         
def training_onKeyHold(app, keys):
    myPlayer = app.players[0]
    if 'escape' in keys:
        setActiveScreen('start')
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
            myPlayer.numJumps -= 1
        elif myPlayer.numJumps == 1:
            currentTime = time.time()
            if currentTime - myPlayer.firstJumpTime > 0.4:
                myPlayer.jump()
                myPlayer.numJumps -= 1
    if 'e' in keys and myPlayer.boostLevel > 0:
        myPlayer.boost()
        myPlayer.isBoosting = True

def training_onKeyRelease(app, key):
    myPlayer = app.players[0]
    if key == 'e':
        myPlayer.isBoosting = False
        myPlayer.boostCooldown = time.time()

def training_onStep(app):
    if app.scored:
        time.sleep(1.5)
        training_onScreenActivate(app)
    app.ball.updatePosition(app)
    if ((app.ball.cx + app.ball.r >= app.mapRight 
    or app.ball.cx - app.ball.r <= app.mapLeft)
    and app.topGoalY + app.ball.r <= app.ball.cy <= app.bottomGoalY - app.ball.r):
        app.scored = True
    myPlayer = app.players[0]
    myPlayer.updateBoostState()
    myPlayer.checkAirborne()
    myPlayer.updateMovement()
    app.ball.handlePlayerCollision(myPlayer)
    if not myPlayer.inAir:
        myPlayer.decelerate()

#END TRAINING MODE
#1v1 PLAYER MODE

def oneVPlayer_onScreenActivate(app):
    app.players = [Player(200,app.mapBottom - 10, 0,'blue', app), 
    Player(app.width - 200, app.mapBottom - 10, 0, 'orange', app)]
    app.ball = Ball(app.width//2, app.height//2, app)
    app.timer = 120 #2 min timer
    app.blueScore = 0
    app.orangeScore = 0
    app.countdown = 240
    app.counter = 0
    app.scored = False

def activateKickoff(app):
    app.scored = False
    app.countdown = 240
    player1 = app.players[0]
    player2 = app.players[1]
    player1.cx = 200
    player1.cy = app.mapBottom - 20
    player1.vx, player1.vy = 0, 0
    player1.dir = 0
    player1.boostLevel = 33
    player2.cx = app.width - 200
    player2.cy = app.mapBottom - 20
    player2.dir = 0
    player2.vx, player2.vy = 0, 0
    player2.boostLevel = 33
    app.ball.cx, app.ball.cy = app.width//2, app.height//2
    app.ball.vx, app.ball.vy = 0, 0

def oneVPlayer_redrawAll(app):
    drawLabel(f'{app.timer//60}:{app.timer%60}', app.width/2, 20, size = 30, font = 'monospace')
    drawLabel('Esc to return', 100, 50, size = 20, font = 'monospace')
    drawLabel(f'Blue: {app.blueScore}', 250, 50, size = 30, 
                fill = 'blue', font = 'monospace')
    drawLabel(f'Orange: {app.orangeScore}', app.width - 250, 50, size = 30, 
                fill = 'orange', font = 'monospace')
    drawMap(app)
    drawPlayers(app)
    drawBall(app)
    if app.countdown > 1:
        drawLabel(app.countdown // 60, app.width/2, app.height/2, size = 50,
                font = 'monospace')
    if app.scored:
        drawLabel('GOAL!', app.width/2, app.height/2, size = 50, 
        font = 'monospace', fill = gradient('orange','blue',start = 'left'))
    if app.timer == 0:
        if app.blueScore == app.orangeScore:
            drawLabel('Tie! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 50, font = 'monospace')
        elif app.blueScore > app.orangeScore:
            drawLabel('Blue Wins! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 50, font = 'monospace')
        else:
            drawLabel('Orange Wins! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 50, font = 'monospace')
            
def oneVPlayer_onKeyHold(app, keys):
    player1 = app.players[0]
    player2 = app.players[1]
    if app.countdown == 0:
        if 'd' in keys and not player1.inAir:
            player1.moveRight()
        elif 'a' in keys and not player1.inAir:
            player1.moveLeft()
        if 'w' in keys and player1.inAir:
            player1.rotate(5)
        if 's' in keys and player1.inAir:
            player1.rotate(-5)
        if 'space' in keys:
            if not player1.inAir:
                player1.jump() 
                player1.firstJumpTime = time.time()
                player1.numJumps -= 1
            elif player1.numJumps == 1:
                currentTime = time.time()
                if currentTime - player1.firstJumpTime > 0.4:
                    player1.jump()
                    player1.numJumps -= 1
        if 'e' in keys and player1.boostLevel > 0:
            player1.boost()
            player1.isBoosting = True
        
        if 'l' in keys and not player2.inAir:
            player2.moveRight()
        elif 'j' in keys and not player2.inAir:
            player2.moveLeft()
        if 'i' in keys and player2.inAir:
            player2.rotate(5)
        if 'k' in keys and player2.inAir:
            player2.rotate(-5)
        if 'o' in keys:
            if not player2.inAir:
                player2.jump() 
                player2.firstJumpTime = time.time()
                player2.numJumps -= 1
            elif player2.numJumps == 1:
                currentTime = time.time()
                if currentTime - player2.firstJumpTime > 0.4:
                    player2.jump()
                    player2.numJumps -= 1
        if 'n' in keys and player2.boostLevel > 0:
            player2.boost()
            player2.isBoosting = True
    if 'escape' in keys:
        setActiveScreen('start')
    if 'r' in keys:
        setActiveScreen('oneVPlayer')

def oneVPlayer_onKeyRelease(app, keys):
    player1 = app.players[0]
    player2 = app.players[1]
    if 'e' in keys:
        player1.isBoosting = False
        player1.boostCooldown = time.time()
    if 'n' in keys:
        player2.isBoosting = False
        player2.boostCooldown = time.time()

def oneVPlayer_onStep(app):
    if app.timer != 0 and app.countdown == 0:
        if app.scored:
            time.sleep(1.5)
            activateKickoff(app)
        if app.counter % 60 == 1:
            app.timer -= 1
        if (app.ball.cx + app.ball.r >= app.mapRight and 
        app.topGoalY + app.ball.r <= app.ball.cy <= app.bottomGoalY - app.ball.r):
            app.scored = True
            app.blueScore +=1
        if (app.ball.cx - app.ball.r <= app.mapLeft and 
        app.topGoalY + app.ball.r <= app.ball.cy <= app.bottomGoalY - app.ball.r):
            app.scored = True
            app.orangeScore +=1
        app.ball.updatePosition(app)
        for player in app.players:
            player.updateBoostState()
            player.checkAirborne()
            player.updateMovement()
            app.ball.handlePlayerCollision(player)
            if not player.inAir:
                player.decelerate()
        app.counter += 1
    elif app.countdown > 0:
        app.countdown -= 1

#END 1v1 PLAYER MODE
#GENERAL FUNCTIONS

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
        if circle == app.BRCircle or circle == app.TRCircle:
            teamColor= 'orange'
        else:
            teamColor = 'blue'
        drawArc(circle[0], circle[1], app.cornerRadius*2+4, 
                app.cornerRadius*2+4, startAngle, sweepAngle, 
                fill=None, border=teamColor, borderWidth=borderWidth)
        startAngle+=90
    
    #Fill in corners
    for circle in app.circles:
        drawCircle(circle[0], circle[1], 
                   app.cornerRadius-3, fill='white')

    #Blue and Orange goals
    drawLine(25, app.topGoalY, 25, app.bottomGoalY, fill='blue', lineWidth=15)
    drawLine(app.width-25, app.topGoalY, app.width-25, app.bottomGoalY, 
            fill='orange', lineWidth=15)

    #Midfield point
    drawLine(app.width/2-10, app.height-75, app.width/2+10, app.height-75, 
            fill='red',lineWidth=10)

def drawPlayers(app):
    boostX = 50
    for player in app.players:
        wheelR = 7
        grad = gradient(player.team,'black', start='top')
        drawRect(player.cx-player.width/2,player.cy-player.height/2,player.width,
                 player.height, fill=grad,rotateAngle=player.dir)
        # drawCircle(player.cx + wheelR - 25 * math.cos(math.radians(player.dir)),
        #             player.cy + wheelR/2 - 25 * math.sin(math.radians(player.dir)), wheelR)
        normal = 90 - player.dir
        drawLine(player.cx, player.cy,player.cx + 50 * math.cos(math.radians(normal)), 
                player.cy - 50 * math.sin(math.radians(normal)))
        if player.isBoosting:
            if not player.inAir:
                drawCircle(player.cx - player.vx // 5, 
                player.cy - player.vy // 5, 20, fill = player.team)
            else:
                drawCircle(player.cx - 50 * math.cos(math.radians(player.dir)), 
                 player.cy - 50 * math.sin(math.radians(player.dir)), 20, fill = player.team)
        startAngle = 0
        sweepAngle = rounded(player.boostLevel * (360/100))
        if sweepAngle != 0:
            drawArc(boostX,app.height-50, 50, 50, startAngle, sweepAngle, fill=player.team)
        drawLabel(player.boostLevel, boostX, app.height-50, size = 30, 
        font = 'monospace', bold = True, fill = 'black')
        boostX += app.width - 100

def main():
    runAppWithScreens(initialScreen='start')

main()