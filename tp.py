from cmu_graphics import *
import numpy as np
import player

def onAppStart(app):
    app.width = 1200
    app.height = 800

def redrawAll(app):
    drawMap(app)

def drawMap(app):
    drawRect(25, 75, app.width-50, app.height-150, 
            fill=None, border='black', borderWidth=5)
    #Blue and Orange goals
    topGoalY=app.height/2+100
    bottomGoalY=app.height/2-100
    drawLine(25, topGoalY, 25, bottomGoalY, fill='blue', lineWidth=15)
    drawLine(app.width-25, topGoalY, app.width-25, bottomGoalY, 
            fill='orange', lineWidth=15)

    drawLine(app.width/2-10, app.height-75, app.width/2+10, app.height-75, 
            fill='red',lineWidth=10)
runApp()