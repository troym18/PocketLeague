from cmu_graphics import *
def onAppStart(app):
    app.width=900
    app.height=600
def redrawAll(app):
    drawMap(app)

def drawMap(app):
    drawRect(50,50,800,500,fill=None,border='black',borderWidth=5)
    drawArc(75,75,50,50,90,90,fill=None,border='black',borderWidth=5)
runApp()