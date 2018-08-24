import random

from production.coordinate import Coordinates
from production.direction_error import DirectionError

emptyField = """ -------------------- 
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
 -------------------- """

class Snake(object):
    
    #untested
    def start(self):
        print self.draw(self.snakePosition)
        direction = ""
        while direction != 'Q':
            direction = raw_input("Which direction do you want to move? Enter L, R, D, U for Left, Right, Down, Up, or Q to Quit!")
            try:
                self.move(direction)
            except DirectionError as dirErr:
                print dirErr.message
                raw_input("Please provide a valid direction.\nWhich direction do you want to move? Enter L, R, D, U for Left, Right, Down, Up or Q to Quit!")
            print self.draw(self.snakePosition)
    #untested

    def __init__(self):
        self.directionModifiers = {'R': Coordinates(1,0), 'L': Coordinates(-1,0), 'U': Coordinates(0,-1), 'D': Coordinates(0,1) }
        head = self.generateRandomHeadCoordinates()
        self.snakePosition = [head]
        tail = [Coordinates(head.x - i, head.y) for i in range(1,5)]
        self.snakePosition.extend(tail)
    
    def draw(self, snakePositions):
        gameMap = emptyField
        if(snakePositions is not None):
            mapLines = gameMap.split("\n")
            for coord in snakePositions:
                line = list(mapLines[coord.y])
                for i in range(len(line)):
                    if i == coord.x:
                        line[i] = '@'
                mapLines[coord.y] = "".join(line)
            gameMap = "\n".join(mapLines)
        return gameMap
    
    def generateRandomHeadCoordinates(self):
        return Coordinates(random.randint(6,19), random.randint(1,20))
    
    def setCoordinates(self, coordinates):
        self.snakePosition = coordinates
        
    def getCoordinates(self):
        return self.snakePosition
        
    def move(self, direction):
        if direction not in ['R', 'L', 'U', 'D']:
            raise DirectionError("Unexpected direction: '{0}' !".format(direction))
        newHead = self.snakePosition[0] + self.directionModifiers[direction]
        if newHead == self.snakePosition[1]:
            raise DirectionError("Snake cannot go in direction of body!")            
        self.snakePosition.pop()
        newTail = self.snakePosition
        self.snakePosition = [newHead]
        self.snakePosition.extend(newTail)
        
