from cmu_graphics import *
def onAppStart(app):
    app.width=1200
    app.height=800

def redrawAll(app):
    drawMap(app)

def drawMap(app):
    drawRect(25,75,app.width-50,app.height-150,fill=None,border='black',borderWidth=5)
    drawLine(25,300,25,500,fill='blue',lineWidth=15)
    drawLine(app.width-25,300,app.width-25,500,fill='orange',lineWidth=15)
    drawLine(app.width/2-10,app.height-75,app.width/2+10,app.height-75,fill='red',lineWidth=10)
runApp()