class Map:
    def __init__(self,app):
        self.left = 25
        self.top = 75
        self.right = app.width - 50
        self.bottom = app.height - 25