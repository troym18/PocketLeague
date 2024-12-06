from cmu_graphics import *
from player import Player
from ball import Ball
from PowerUps import powerUp
from PIL import Image, ImageFont, ImageDraw
import random
import time
import math
import os

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    app.mapTop = 50
    app.mapLeft = 25
    app.cornerRadius = 100
    app.mapRight = app.width - 25
    app.mapBottom = app.height - 75
    app.topGoalY = app.height/2 - 125
    app.bottomGoalY = app.height/2 + 175
    app.TRCircle = [app.mapRight - app.cornerRadius, 
                    app.mapTop + app.cornerRadius]
    app.TLCircle = [app.mapLeft + app.cornerRadius, 
                    app.mapTop + app.cornerRadius]
    app.BLCircle = [app.mapLeft  + app.cornerRadius, 
                    app.mapBottom - app.cornerRadius]
    app.BRCircle = [app.mapRight - app.cornerRadius, 
                    app.mapBottom - app.cornerRadius]
    app.circles = [app.TRCircle, app.TLCircle, app.BLCircle, app.BRCircle]
    app.ballState = 0
    app.counter = 0
    app.gravity = 200
#START

def loadAllImages(app):
    currDir = os.path.dirname(os.path.realpath(__file__)) + '/images'
    app.gameDescription = CMUImage(Image.open(currDir + '/GameDescription.png'))
    app.keybindsDescription = CMUImage(Image.open(currDir + '/KeybindDescription.png'))
    app.blue = CMUImage(Image.open(currDir + '/Blue.png'))
    app.blueBoost = CMUImage(Image.open(currDir + '/BlueBoost.png'))
    app.blueInverted = CMUImage(Image.open(currDir + '/BlueInverted.png'))
    app.blueBoostInverted = CMUImage(Image.open(currDir + '/BlueBoostInverted.png'))
    app.orange = CMUImage(Image.open(currDir + '/Orange.png'))
    app.orangeBoost = CMUImage(Image.open(currDir + '/OrangeBoost.png'))
    app.orangeInverted = CMUImage(Image.open(currDir + '/OrangeInverted.png'))
    app.orangeBoostInverted = CMUImage(Image.open(currDir + '/OrangeBoostInverted.png'))
    app.GrayBoost = CMUImage(Image.open(currDir + '/GrayBoost.png'))
    app.GrayBoostInverted = CMUImage(Image.open(currDir + '/GrayBoostInverted.png'))
    app.mainMenu = CMUImage(Image.open(currDir + '/MainMenu.jpg'))
    app.Gray = CMUImage(Image.open(currDir + '/Gray.png'))
    app.GrayInverted = CMUImage(Image.open(currDir + '/GrayInverted.png'))
    ballBase = currDir + '/Ball'
    app.ballSprites = [CMUImage(Image.open(ballBase+f'{i}.png')) for i in range(4)]
    app.backgroundImage = CMUImage(Image.open(currDir + '/GameBackground.webp'))
    app.titleScreen = CMUImage(Image.open(currDir + '/GameTitle.jpg'))
    app.titleText = CMUImage(Image.open(currDir + '/Title.png'))
    bigFont = ImageFont.truetype(currDir + '/GoGoPosterPunch.ttf', 42) 
    img = Image.new('RGB', (300, 75), (65, 105, 225))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(currDir + '/GoGoPosterPunch.ttf', 28) 
    draw.text((150, 37.5), "Training Mode", font = font, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path =currDir + '/TrainingMode.png'
    img.save(path)
    app.trainingMode = CMUImage(Image.open(path))
    img = Image.new('RGB', (300, 75), (65, 105, 225))
    draw = ImageDraw.Draw(img)
    draw.text((150, 37.5), "Multiplayer Mode", font = font, 
            fill=(255, 255, 255), anchor="mm", 
            stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/MultiplayerMode.png'
    img.save(path)
    app.multiplayerMode = CMUImage(Image.open(path))
    img = Image.new('RGB', (300, 75), (65, 105, 225))
    draw = ImageDraw.Draw(img)
    draw.text((150, 37.5), "How To Play", font = font, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/HowTo.png'
    img.save(path)
    app.howTo = CMUImage(Image.open(path))
    img = Image.new('RGB', (300, 75), (65, 105, 225))
    draw = ImageDraw.Draw(img)
    draw.text((150, 37.5), "Keybinds", font = font, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/Keybinds.png'
    img.save(path)
    app.keybinds = CMUImage(Image.open(path))
    img = Image.new('RGB', (300, 75), (65, 105, 225))
    draw = ImageDraw.Draw(img)
    draw.text((150, 37.5), "1 v 1 (Player)", font = font, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/1v1Player.png'
    img.save(path)
    app.oneVPlayer = CMUImage(Image.open(path))
    img = Image.new('RGB', (300, 75), (65, 105, 225))
    draw = ImageDraw.Draw(img)
    draw.text((150, 37.5), "1 v 1 (Power Ups)", font = font, 
            fill=(255, 255, 255), anchor="mm", stroke_fill = (0,0,0), 
            stroke_width = 3)
    path = currDir + '/1v1PowerUps.png'
    img.save(path)
    app.oneVPowerUp = CMUImage(Image.open(path))
    img = Image.new('RGB', (500, 100), (170, 170, 170))
    draw = ImageDraw.Draw(img)
    draw.text((250, 50), "Multiplayer Modes", font = bigFont, 
            fill=(255, 255, 255), anchor="mm", stroke_fill = (0,0,0), 
            stroke_width = 3)
    path = currDir + '/MultiplayerModes.png'
    img.save(path)
    app.multiplayerModeTitle = CMUImage(Image.open(path))
    img = Image.new('RGB', (500, 100), (170, 170, 170))
    draw = ImageDraw.Draw(img)
    draw.text((250, 50), "Instructions", font = bigFont, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/Instructions.png'
    img.save(path)
    app.instructionsTitle = CMUImage(Image.open(path))
    img = Image.new('RGB', (500, 100), (170, 170, 170))
    draw = ImageDraw.Draw(img)
    draw.text((250, 50), "Keybinds", font = bigFont, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/KeybindsTitle.png'
    img.save(path)
    app.keybindsTitle = CMUImage(Image.open(path))
    img = Image.new('RGB', (300, 75), (170, 170, 170))
    draw = ImageDraw.Draw(img)
    draw.text((150, 37.5), "Power Ups", font = font, fill=(255, 255, 255), 
            anchor="mm", stroke_fill = (0,0,0), stroke_width = 3)
    path = currDir + '/PowerUpsTitle.png'
    img.save(path)
    app.powerUpsTitle = CMUImage(Image.open(path))


def start_onScreenActivate(app):
    app.hoverTraining = False
    app.hoverMultiplayer = False
    app.hoverHowTo = False
    loadAllImages(app)

def start_redrawAll(app):
    titleWidth, titleHeight = getImageSize(app.titleText)
    buttonWidth = 300
    buttonHeight = 75
    drawImage(app.titleScreen, 0, 0, width = app.width, height = app.height)
    drawImage(app.titleText, app.width/2 - 0.75 * titleWidth, 200, 
            width = 1.5 * titleWidth, height = 1.5 * titleHeight)
    if app.hoverTraining:
        drawRect(95, app.height - 105, buttonWidth + 10, buttonHeight + 10, 
            fill = None, border = 'black', borderWidth = 20)
    drawImage(app.trainingMode, 100, app.height - 100)
    if app.hoverMultiplayer:
        drawRect(app.width/2 - buttonWidth/2 - 5 , app.height - 105, 
        buttonWidth + 10, buttonHeight + 10, fill = None, 
        border = 'black', borderWidth = 20)
    drawImage(app.multiplayerMode, app.width/2 - buttonWidth/2 , 
              app.height - 100)
    if app.hoverHowTo:
        drawRect(795, app.height - 105, buttonWidth + 10, buttonHeight + 10, 
        fill = None, border = 'black', borderWidth = 20)
    drawImage(app.howTo, 800, app.height - 100)

def start_onMousePress(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (100 <= mouseX <= 100 + buttonWidth and
        app.height - 100 <= mouseY <= app.height - 100 + buttonHeight):
        setActiveScreen('training')
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        app.height - 100 <= mouseY <= app.height - 100 + buttonHeight):
        setActiveScreen('multiplayerStart')
    if (800 <= mouseX <= 800 + buttonWidth and
        app.height - 100 <= mouseY <= app.height - 100 + buttonHeight):
        setActiveScreen('instructions')

def start_onMouseMove(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (100 <= mouseX <= 100 + buttonWidth and
        app.height - 100 <= mouseY <= app.height - 100 + buttonHeight):
        app.hoverTraining = True
    else:
        app.hoverTraining = False
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        app.height - 100 <= mouseY <= app.height - 100 + buttonHeight):
        app.hoverMultiplayer = True
    else:
        app.hoverMultiplayer = False
    if (800 <= mouseX <= 800 + buttonWidth and
        app.height - 100 <= mouseY <= app.height - 100 + buttonHeight):
        app.hoverHowTo = True
    else:
        app.hoverHowTo = False

#END START
#INSTRUCTIONS
def instructions_onScreenActivate(app):
    app.hoverKeybinds = False
    app.powerUps = [powerUp(app, 300, app.height - 100, "speed"),
                    powerUp(app, 500, app.height - 100, "boost"),
                    powerUp(app, 700, app.height - 100, "swap"),
                    powerUp(app, 900, app.height - 100, "gravity")]

def instructions_redrawAll(app):
    drawImage(app.mainMenu, 0, 0, width = app.width, height = app.height)

    buttonWidth = 300
    buttonHeight = 75

    drawImage(app.instructionsTitle, app.width / 2 - 250, 0)
    drawImage(app.gameDescription, 100, 100, width = 1000, height = 300)

    drawImage(app.powerUpsTitle, app.width/2 - buttonWidth/2 , 575)
    if app.hoverKeybinds:
        drawRect(app.width / 2 - buttonWidth / 2 - 5, 445, buttonWidth + 10, 
             buttonHeight + 10, fill=None, border="black", borderWidth = 10)
    drawImage(app.keybinds, app.width / 2 - buttonWidth/2, 450)
    drawLabel("Esc to return", 100, 50, size=20)
    drawLabel("Speed Boost", 300, app.height - 130, 
            size = 20, fill = gradient('red', 'orange', start = 'center'))
    drawLabel("Increase Driving Speed", 300, app.height - 70, 
            size = 20, fill = gradient('red', 'orange', start = 'center'))
    drawLabel("Boost Refill", 500, app.height - 130, 
            size = 20, fill = gradient('yellow', 'white', start = 'center'))
    drawLabel("Set Boost to 100", 500, app.height - 70, 
            size = 20, fill = gradient('yellow', 'white', start = 'center'))
    darkerGreen = rgb(0, 50, 0)
    drawLabel("Teleport", 700, app.height - 130, 
            size = 20, fill = gradient('lightGreen', 'white', start = 'center'))
    drawLabel("Swap Positions", 700, app.height - 70, 
            size = 20, fill = gradient('lightGreen', 'white', start = 'center'))
    drawLabel("Gravity", 900, app.height - 130, 
            size = 20, fill = gradient('purple', 'white', start = 'center'))
    drawLabel("Reverse Gravity", 900, app.height - 70, 
            size = 20, fill = gradient('purple', 'white', start = 'center'))
    for powerUp in app.powerUps:
        if powerUp.active:
            powerUp.draw()


def instructions_onMousePress(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        450 <= mouseY <= 450 + buttonHeight):
        setActiveScreen('keybinds')

def instructions_onMouseMove(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        450 <= mouseY <= 450 + buttonHeight):
        app.hoverKeybinds = True
    else:
        app.hoverKeybinds = False
    
    
def instructions_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

#INSTRUCTIONS END
#KEYBINDS

def keybinds_redrawAll(app):
    drawImage(app.mainMenu, 0, 0, width = app.width, height = app.height)
    drawImage(app.keybindsTitle, app.width / 2 - 250, 0)
    drawImage(app.keybindsDescription, 100, 100, width = 1000, height = 700)
    drawLabel('Esc to return', 100, 50, size = 20, font = 'arial')

def keybinds_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

#END KEYBINDS
#MULTIPLAYER START

def multiplayerStart_onScreenActivate(app):
    app.hover1v1 = False
    app.hoverPowerUp = False

def multiplayerStart_redrawAll(app):
    drawImage(app.mainMenu, 0, 0, width = app.width, height = app.height)
    buttonWidth = 300
    buttonHeight = 75
    drawImage(app.multiplayerModeTitle, app.width/2 - 250, 0)
    if app.hover1v1:
        drawRect(app.width/2 - buttonWidth/2 - 5, 195, buttonWidth + 10, 
            buttonHeight + 10, fill = None, border = 'black', borderWidth = 20)
    drawImage(app.oneVPlayer, app.width/2 - buttonWidth/2, 200)
    if app.hoverPowerUp:
        drawRect(app.width/2 - buttonWidth/2 - 5, 345, buttonWidth + 10,
        buttonHeight + 10, fill = None, border = 'black', borderWidth = 20)
    drawImage(app.oneVPowerUp, app.width/2 - buttonWidth/2, 350)
    drawLabel('Esc to return', 100, 50, size = 20, font = 'arial')

def multiplayerStart_onKeyPress(app, key):
    if key == 'escape':
        setActiveScreen('start')

def multiplayerStart_onMousePress(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        200 <= mouseY <= 200 + buttonHeight):
        setActiveScreen('oneVPlayer')
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        350 <= mouseY <= 350 + buttonHeight):
        setActiveScreen('powerups')

def multiplayerStart_onMouseMove(app, mouseX, mouseY):
    buttonWidth = 300
    buttonHeight = 75
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        200 <= mouseY <= 200 + buttonHeight):
        app.hover1v1 = True
    else:
        app.hover1v1 = False
    if (app.width/2 - buttonWidth/2 <= mouseX <= app.width/2 + buttonWidth/2 and
        350 <= mouseY <= 350 + buttonHeight):
        app.hoverPowerUp = True
    else:
        app.hoverPowerUp = False

#END MULTIPLAYER START
#TRAINING MODE

def training_onScreenActivate(app):
    app.players =[Player(200, app.mapBottom - 10,0, 'Gray', app)]
    app.ball = Ball(app.width//2, app.height//2, app)
    app.scored = False
    app.delay = 0
    app.closeScore = False

def training_redrawAll(app):
    drawMap(app)
    drawRect(30, 35, 140, 30, fill = 'gray')
    drawLabel('Esc to return', 100, 50, size = 20, font = 'arial', 
              fill = 'white')
    drawRect(app.width/2 - 150, 0, 300, 40, fill = 'white')
    drawLabel("Training Mode", app.width/2, 20, size = 30, font = 'arial', 
              fill = 'black')
    drawPlayers(app)
    drawBall(app)
    if app.scored:
        drawLabel('GOAL!', app.width/2, app.height/2, size = 50, 
        font = 'arial', fill = gradient('orange','blue',start = 'left'))
    if app.closeScore:
        drawLabel(f'Close Call!', app.width/2, app.height - 50, size = 30, 
                  font = 'arial')
         
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
    if (app.ball.cx + app.ball.r >= app.mapRight or 
          app.ball.cx - app.ball.r <= app.mapLeft and 
          app.topGoalY <= app.ball.cy <= app.bottomGoalY):
        if (app.topGoalY + app.ball.r <= app.ball.cy 
            <= app.bottomGoalY - app.ball.r):
            app.scored = True
        else:
            app.closeScore = True
            app.delay = time.time()
    myPlayer = app.players[0]
    myPlayer.updateBoostState()
    myPlayer.checkAirborne()
    myPlayer.updateMovement()
    app.ball.handlePlayerCollision(myPlayer)
    if myPlayer.boostLevel <= 0:
                myPlayer.isBoosting = False
    if not myPlayer.inAir:
        myPlayer.decelerate()
    currentTime = time.time()
    if abs(currentTime - app.delay) > 1:
        app.closeScore = False
    ballSpeed = rounded(math.sqrt(app.ball.vx ** 2 + app.ball.vy ** 2))
    updateRate = max(8, 120 - int(ballSpeed * 3))
    if app.counter % updateRate == 0:
        app.ballState = (app.ballState + 1) % 4
    app.counter += 1

#END TRAINING MODE
#1v1 PLAYER MODE

def oneVPlayer_onScreenActivate(app):
    app.players = [Player(200,app.mapBottom - 10, 0,'Blue', app), 
    Player(app.width - 200, app.mapBottom - 10, 0, 'Orange', app)]
    app.ball = Ball(app.width//2, app.height//2, app)
    app.timer = 120 #2 min timer
    app.blueScore = 0
    app.orangeScore = 0
    app.countdown = 240
    app.scored = False
    app.closeScore = False
    player1 = app.players[0]
    player2 = app.players[1]
    player1.inverted = False
    player2.inverted = True

def oneVPlayer_redrawAll(app):
    drawMap(app)
    drawRect(0, 0, app.width, 40, fill = 'gray')
    drawLabel(f'{app.timer//60}:{app.timer%60}', app.width/2, 20, 
              size = 30, font = 'arial')
    drawLabel('Esc to return', 100, 20, size = 20, 
             font = 'arial', fill = 'white')
    drawLabel(f'Blue: {app.blueScore}', 250, 20, size = 30, 
                fill = 'blue', font = 'arial')
    drawLabel(f'Orange: {app.orangeScore}', app.width - 250, 20, size = 30, 
                fill = 'orange', font = 'arial')
    drawPlayers(app)
    drawBall(app)
    if app.countdown > 1:
        drawLabel(app.countdown // 60, app.width/2, app.height/2, size = 50,
                font = 'arial')
    if app.scored:
        drawLabel('GOAL!', app.width/2, app.height/2, size = 50, 
        font = 'arial', fill = gradient('orange','blue',start = 'left'))
    elif app.closeScore:
        drawLabel('Close Call!', app.width/2, app.height - 50, size = 30, 
                  font = 'arial')
    if app.timer == 0:
        if app.blueScore == app.orangeScore:
            drawLabel('Tie! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 30, font = 'arial')
        elif app.blueScore > app.orangeScore:
            drawLabel('Blue Wins! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 30, font = 'arial')
        else:
            drawLabel('Orange Wins! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 30, font = 'arial')
            
def oneVPlayer_onKeyHold(app, keys):
    player1 = app.players[0]
    player2 = app.players[1]
    if app.countdown == 0 and app.timer != 0:
        if 'd' in keys and not player1.inAir:
            player1.moveRight()
        if 'a' in keys and not player1.inAir:
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
            player1.boostCooldown = time.time()
        if 'right' in keys and not player2.inAir:
            player2.moveRight()
        elif 'left' in keys and not player2.inAir:
            player2.moveLeft()
        if 'up' in keys and player2.inAir:
            player2.rotate(5)
        if 'down' in keys and player2.inAir:
            player2.rotate(-5)
        if '.' in keys:
            if not player2.inAir:
                player2.jump() 
                player2.firstJumpTime = time.time()
                player2.numJumps -= 1
            elif player2.numJumps == 1:
                currentTime = time.time()
                if currentTime - player2.firstJumpTime > 0.4:
                    player2.jump()
                    player2.numJumps -= 1
        if '/' in keys and player2.boostLevel > 0:
            player2.boost()
            player2.isBoosting = True
            player2.boostCooldown = time.time()
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
    if '/' in keys:
        player2.isBoosting = False
        player2.boostCooldown = time.time()

def oneVPlayer_onStep(app):
    if app.timer != 0 and app.countdown == 0:
        if app.scored:
            time.sleep(1.5)
            activateKickoff(app)
        if app.closeScore and app.delay - app.timer > 2:
            app.closeScore = False
        if app.counter % 60 == 1:
            app.timer -= 1
        if (app.ball.cx + app.ball.r >= app.mapRight and 
            app.topGoalY + app.ball.r <= app.ball.cy <= 
            app.bottomGoalY - app.ball.r):
            app.scored = True
            app.blueScore +=1
        elif (app.ball.cx - app.ball.r <= app.mapLeft and 
            app.topGoalY + app.ball.r <= app.ball.cy <= 
            app.bottomGoalY - app.ball.r):
            app.scored = True
            app.orangeScore +=1
        elif (app.ball.cx + app.ball.r >= app.mapRight or 
        app.ball.cx - app.ball.r <= app.mapLeft and 
        app.topGoalY <= app.ball.cy <= app.bottomGoalY):
            app.closeScore = True
            app.delay = app.timer
        app.ball.updatePosition(app)
        for player in app.players:
            if player.boostLevel <= 0:
                player.isBoosting = False
            player.updateBoostState()
            player.checkAirborne()
            player.updateMovement()
            app.ball.handlePlayerCollision(player)
            if not player.inAir:
                player.decelerate()
    elif app.countdown > 0:
        app.countdown -= 1
    ballSpeed = rounded(math.sqrt(app.ball.vx ** 2 + app.ball.vy ** 2))
    updateRate = max(8, 120 - int(ballSpeed * 3))
    if app.counter % updateRate == 0:
        app.ballState = (app.ballState + 1) % 4
    app.counter += 1

#END 1v1 PLAYER MODE
#1v1 POWERUPS MODE

def powerups_onScreenActivate(app):
    app.players = [Player(200,app.mapBottom - 10, 0,'Blue', app), 
    Player(app.width - 200, app.mapBottom - 10, 0, 'Orange', app)]
    app.ball = Ball(app.width//2, app.height//2, app)
    app.timer = 120 #2 min timer
    app.blueScore = 0
    app.orangeScore = 0
    app.countdown = 240
    app.counter = 0
    app.scored = False
    app.closeScore = False
    player1 = app.players[0]
    player2 = app.players[1]
    player1.inverted = False
    player2.inverted = True
    app.powerUps = []

def powerups_redrawAll(app):
    drawMap(app)
    drawRect(0, 0, app.width, 40, fill = 'gray')
    drawLabel(f'{app.timer//60}:{app.timer%60}', app.width/2, 20, 
              size = 30, font = 'arial')
    drawLabel('Esc to return', 100, 20, size = 20, 
             font = 'arial', fill = 'white')
    drawLabel(f'Blue: {app.blueScore}', 250, 20, size = 30, 
                fill = 'blue', font = 'arial')
    drawLabel(f'Orange: {app.orangeScore}', app.width - 250, 20, size = 30, 
                fill = 'orange', font = 'arial')
    drawPlayers(app)
    drawBall(app)
    for powerUp in app.powerUps:
        if powerUp.active:
            powerUp.draw()
    if app.countdown > 1:
        drawLabel(app.countdown // 60, app.width/2, app.height/2, size = 50,
                font = 'arial')
    if app.scored:
        drawLabel('GOAL!', app.width/2, app.height/2, size = 50, 
        font = 'arial', fill = gradient('orange','blue',start = 'left'))
    elif app.closeScore:
        drawLabel('Close Call!', app.width/2, app.height - 50, size = 30, 
                  font = 'arial')
    if app.timer == 0:
        if app.blueScore == app.orangeScore:
            drawLabel('Tie! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 30, font = 'arial')
        elif app.blueScore > app.orangeScore:
            drawLabel('Blue Wins! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 30, font = 'arial')
        else:
            drawLabel('Orange Wins! Esc to go back, r to restart!', app.width/2,
            app.height/2, size = 30, font = 'arial')
            
def powerups_onKeyHold(app, keys):
    player1 = app.players[0]
    player2 = app.players[1]
    if app.countdown == 0 and app.timer != 0:
        if 'd' in keys and not player1.inAir:
            player1.moveRight()
        if 'a' in keys and not player1.inAir:
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
            player1.boostCooldown = time.time()
        if 'right' in keys and not player2.inAir:
            player2.moveRight()
        elif 'left' in keys and not player2.inAir:
            player2.moveLeft()
        if 'up' in keys and player2.inAir:
            player2.rotate(5)
        if 'down' in keys and player2.inAir:
            player2.rotate(-5)
        if '.' in keys:
            if not player2.inAir:
                player2.jump() 
                player2.firstJumpTime = time.time()
                player2.numJumps -= 1
            elif player2.numJumps == 1:
                currentTime = time.time()
                if currentTime - player2.firstJumpTime > 0.4:
                    player2.jump()
                    player2.numJumps -= 1
        if '/' in keys and player2.boostLevel > 0:
            player2.boost()
            player2.isBoosting = True
            player2.boostCooldown = time.time()
    if 'escape' in keys:
        setActiveScreen('start')
    if 'r' in keys:
        setActiveScreen('oneVPlayer')

def powerups_onKeyRelease(app, keys):
    player1 = app.players[0]
    player2 = app.players[1]
    if 'e' in keys:
        player1.isBoosting = False
        player1.boostCooldown = time.time()
    if '/' in keys:
        player2.isBoosting = False
        player2.boostCooldown = time.time()

def powerups_onStep(app):
    if app.timer != 0 and app.countdown == 0:
        checkPowerUpCollision(app)
        i = 0
        while i < len(app.powerUps):
            if ((abs(time.time() - app.powerUps[i].startTime) >= 7 or 
                app.scored) and not app.powerUps[i].active):
                app.powerUps[i].revert(app.powerUps[i].appliedPlayer)
                app.powerUps.pop(i)
            else:
                i +=1
        if app.scored:
            time.sleep(1.5)
            activateKickoff(app)
        if app.closeScore and app.delay - app.timer > 2:
            app.closeScore = False
        if app.counter % 60 == 1:
            app.timer -= 1
        if app.counter % 400 == 1:
            spawnPowerUps(app)
        if (app.ball.cx + app.ball.r >= app.mapRight and 
        app.topGoalY + app.ball.r <= app.ball.cy <= 
        app.bottomGoalY - app.ball.r):
            app.scored = True
            app.blueScore +=1
        elif (app.ball.cx - app.ball.r <= app.mapLeft and 
        app.topGoalY + app.ball.r <= app.ball.cy <= 
        app.bottomGoalY - app.ball.r):
            app.scored = True
            app.orangeScore +=1
        elif (app.ball.cx + app.ball.r >= app.mapRight or 
        app.ball.cx - app.ball.r <= app.mapLeft and 
        app.topGoalY <= app.ball.cy <= app.bottomGoalY):
            app.closeScore = True
            app.delay = app.timer
        app.ball.updatePosition(app)
        for player in app.players:
            if player.boostLevel <= 0:
                player.isBoosting = False
            player.updateBoostState()
            player.checkAirborne()
            player.updateMovement()
            app.ball.handlePlayerCollision(player)
            if not player.inAir:
                player.decelerate()
    elif app.countdown > 0:
        app.countdown -= 1
    ballSpeed = rounded(math.sqrt(app.ball.vx ** 2 + app.ball.vy ** 2))
    updateRate = max(8, 120 - int(ballSpeed * 3))
    if app.counter % updateRate == 0:
        app.ballState = (app.ballState + 1) % 4
    app.counter += 1

def spawnPowerUps(app):
    app.powerUps = [
        powerUp(app, 
                random.randint(app.mapLeft + 30, app.mapRight - 30), 
                random.randint(app.mapTop + 30, app.mapBottom - 30), 
                random.choice(["speed", "boost", "swap", "gravity"]))
    ]

def checkPowerUpCollision(app):
    for powerUp in app.powerUps:
        for i in range(2):
            player1 = app.players[i]
            player2 = app.players[1-i]
            if (distance(player1.cx, player1.cy, powerUp.cx, powerUp.cy) < 
                        powerUp.r + player1.width / 2 and powerUp.active):
                powerUp.apply(player1,player2)
                powerUp.appliedPlayer = player1
                powerUp.active = False


#END 1v1 POWERUPS
#GENERAL FUNCTIONS

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
    player1.inverted = False
    player2.inverted = True
    app.powerUps = []

def drawBall(app):
    drawImage(app.ballSprites[app.ballState], app.ball.cx - app.ball.r, 
        app.ball.cy - app.ball.r, 
        width = 2 * app.ball.r, height = 2 *app.ball.r)

def drawMap(app):
    drawImage(app.backgroundImage, 0, 0, width = app.width, height = app.height)

    drawLine(25, app.topGoalY, 25, app.bottomGoalY, fill='blue', lineWidth=15)
    drawLine(app.width-25, app.topGoalY, app.width-25, app.bottomGoalY, 
            fill='orange', lineWidth=15)

def drawPlayers(app):
    boostX = 50
    for player in app.players:
        color = player.team
        if color == 'Gray':
            boost = app.GrayBoost
            car = app.Gray
            boostInv = app.GrayBoostInverted
            inverted = app.GrayInverted
        elif color == 'Blue':
            boost = app.blueBoost
            car = app.blue
            boostInv = app.blueBoostInverted
            inverted = app.blueInverted
        elif color == 'Orange':
            boost = app.orangeBoost
            car = app.orange
            boostInv = app.orangeBoostInverted
            inverted = app.orangeInverted
        if not player.inverted:
            if player.isBoosting and player.boostLevel > 2:
                drawImage(boost, player.cx-player.width/2 - 20,
                          player.cy-player.height/2 - 3,
                          width =player.width + 20, 
                          height = player.height + 3, rotateAngle=player.dir)
            else:
                drawImage(car,player.cx-player.width/2,
                          player.cy-player.height/2,
                          width =player.width, 
                          height = player.height, rotateAngle=player.dir)
        else:
            if player.isBoosting and player.boostLevel > 2:
                drawImage(boostInv,player.cx-player.width/2,
                          player.cy-player.height/2 - 3,
                          width =player.width + 20, 
                          height = player.height + 3, rotateAngle=player.dir)
            else:
                drawImage(inverted, player.cx-player.width/2,
                          player.cy-player.height/2,
                          width =player.width, height = player.height, 
                          rotateAngle=player.dir)

        startAngle = 0
        sweepAngle = rounded(player.boostLevel * (360/100))
        if sweepAngle != 0:
            drawArc(boostX,app.height-50, 50, 50, startAngle, 
                    sweepAngle, fill=(player.team).lower())
        drawLabel(player.boostLevel, boostX, app.height-50, size = 30, 
        bold = True, fill = 'black')
        boostX += app.width - 100

def main():
    runAppWithScreens(initialScreen='start')

main()

#CREDITS
#Title Background: https://sideswipe.rocketleague.com/en/
#Font: GoGoPosterPunch https://www.dafont.com/gogoposterpunch.font
#Game Background: https://sideswipe.rocketleague.com/en/ (In Game)
#Menu Background: https://wall.alphacoders.com/big.php?i=863539
#Car Sprites: https://www.reddit.com/r/RLFashionAdvice/comments/rc17pd/do_u_guys_have_any_clean_or_sweaty_ish_octane_or/
#Ball Sprites: https://sketchfab.com/3d-models/ball-rocket-league-2c8911aa1dcd4c53bad842f2d354dfe2