class Coordinates(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return "[x:{0},y:{1}]".format(self.x, self.y)
    
    def __repr__(self):
        return "[x:{0},y:{1}]".format(self.x, self.y)