import random

from production.coordinate import Coordinates
from production.direction_error import DirectionError
from production.boundaries_error import BoundariesError

banner = """ .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | _____  _____ | || |   ______     | || |  _________   | || |  _______     | |
| |   /  ___  |  | || ||_   _||_   _|| || |  |_   __ \   | || | |_   ___  |  | || | |_   __ \    | |
| |  |  (__ \_|  | || |  | |    | |  | || |    | |__) |  | || |   | |_  \_|  | || |   | |__) |   | |
| |   '.___`-.   | || |  | '    ' |  | || |    |  ___/   | || |   |  _|  _   | || |   |  __ /    | |
| |  |`\____) |  | || |   \ `--' /   | || |   _| |_      | || |  _| |___/ |  | || |  _| |  \ \_  | |
| |  |_______.'  | || |    `.__.'    | || |  |_____|     | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | ____  _____  | || |      __      | || |  ___  ____   | || |  _________   | |
| |   /  ___  |  | || ||_   \|_   _| | || |     /  \     | || | |_  ||_  _|  | || | |_   ___  |  | |
| |  |  (__ \_|  | || |  |   \ | |   | || |    / /\ \    | || |   | |_/ /    | || |   | |_  \_|  | |
| |   '.___`-.   | || |  | |\ \| |   | || |   / ____ \   | || |   |  __'.    | || |   |  _|  _   | |
| |  |`\____) |  | || | _| |_\   |_  | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  _| |___/ |  | |
| |  |_______.'  | || ||_____|\____| | || ||____|  |____|| || | |____||____| | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """

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

directionModifiers = {'R': Coordinates(1,0), 'L': Coordinates(-1,0), 'U': Coordinates(0,-1), 'D': Coordinates(0,1) }
borders = range(1,21)

class Snake(object):
    
    #untested
    def start(self):
        direction = ""
        print banner
        while direction != 'Q':
            print self.draw(self.snakePosition, self.foodPositions)
            direction = raw_input("Which direction do you want to move? Enter L, R, D, U for Left, Right, Down, Up, or Q to Quit!")
            try:
                self.move(direction)
            except DirectionError as dirErr:
                print dirErr.message
                raw_input("Please provide a valid direction.\nWhich direction do you want to move? Enter L, R, D, U for Left, Right, Down, Up or Q to Quit!")
            except BoundariesError as boundErr:
                print self.crashIntoWall(direction)
                print boundErr.message
                break
        print "Quitting game..."
    #untested

    def __init__(self):
        head = self.generateRandomHeadCoordinates()
        self.snakePosition = [head]
        tail = [Coordinates(head.x - i, head.y) for i in range(1,5)]
        self.snakePosition.extend(tail)
        self.foodPositions = list()
        self.generateRandomFoodCoordinates(4)
     
    #this one function is super ugly. test it, refactor it later    
    def crashIntoWall(self, direction):
        return self.__replaceSymbolsInPositionsOnMap('X', [self.snakePosition[0] + directionModifiers[direction]], self.draw(self.snakePosition, self.foodPositions))
    
    def draw(self, snakePosition, foodPositions):
        gameMap = emptyField
        if(snakePosition is not None):
            gameMap = self.__replaceSymbolsInPositionsOnMap('@', snakePosition, gameMap)
        if(foodPositions is not None):
            gameMap = self.__replaceSymbolsInPositionsOnMap('*', foodPositions, gameMap)
        return gameMap
    
    def __replaceSymbolsInPositionsOnMap(self, symbol, positions, gameMap):
        mapLines = gameMap.split("\n")
        for coord in positions:
            line = list(mapLines[coord.y])
            for i in range(len(line)):
                if i == coord.x:
                    line[i] = symbol
            mapLines[coord.y] = "".join(line)
        gameMap = "\n".join(mapLines)
        return gameMap
            
    def generateRandomHeadCoordinates(self):
        return Coordinates(random.randint(6,19), random.randint(1,20))

    def generateRandomFoodCoordinates(self, quantity):
        for i in range(quantity):
            self.foodPositions.append(self.__createValidFoodCoordinates())
    
    def __createValidFoodCoordinates(self):
        while True:
            foodPosition = Coordinates(random.randint(1,20), random.randint(1,20))
            if (foodPosition not in self.snakePosition) and (foodPosition not in self.foodPositions):
                return foodPosition
    
    def setSnakeCoordinates(self, coordinates):
        self.snakePosition = coordinates
        
    def getSnakeCoordinates(self):
        return self.snakePosition
    
    def setFoodCoordinates(self, coordinates):
        self.foodPositions = coordinates
    
    def getFoodCoordinates(self):
        return self.foodPositions
        
    def move(self, direction):
        if direction not in ['R', 'L', 'U', 'D', 'Q']:
            raise DirectionError("Unexpected direction: '{0}' !".format(direction))
        if direction != 'Q':
            newHead = self.snakePosition[0] + directionModifiers[direction]
            if newHead.y not in borders or newHead.x not in borders:
                raise BoundariesError("Snake crashed into wall and died!")
            if newHead == self.snakePosition[1]:
                raise DirectionError("Snake cannot go in direction of body!")            
            if newHead in self.foodPositions:
                self.foodPositions.remove(newHead)
            else:
                self.snakePosition.pop()
            newTail = self.snakePosition
            self.snakePosition = [newHead]
            self.snakePosition.extend(newTail)
            if len(self.foodPositions) < 4:
                self.generateRandomFoodCoordinates(1)
        
