import unittest

from production.coordinate import Coordinates
from production.snake import Snake
from production.direction_error import DirectionError


class Test(unittest.TestCase):
    
    def __setUpSnakeForMovingUpDownRight(self):
        snake = Snake()
        snake.setCoordinates([Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10), Coordinates(10,10)])
        return snake

    def __setUpSnakeForMovingLeftRightUp(self):
        snake = Snake()
        snake.setCoordinates([Coordinates(10,10), Coordinates(10,11), Coordinates(10,12), Coordinates(10,13), Coordinates(10,14)])
        return snake

    def __formatExpectedActual(self, expected, actual):
        return "Expected: {0} \nActual {1} ".format(expected, actual)

    def testDrawMap(self):
        expected = """ -------------------- 
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
        snake = Snake()
        actual = snake.draw(None)
        self.assertMultiLineEqual(expected, actual, "Expected:\n\n{0}\nActual:\n\n{1}".format(expected, actual))
        
    def testDrawSnakeHorizontal(self):
        expected = """ -------------------- 
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|     @@@@@          |
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
        snake = Snake()
        snakePositions = [Coordinates(10,10), Coordinates(9,10), Coordinates(8,10), Coordinates(7,10), Coordinates(6,10)]
        actual = snake.draw(snakePositions)
        self.assertMultiLineEqual(expected, actual, "Expected:\n\n{0}\nActual:\n\n{1}".format(expected, actual))
        
    def testDrawSnakeTurningBack(self):
        expected = """ -------------------- 
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|        @@          |
|         @          |
|        @@          |
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
        snake = Snake()
        snakePositions = [Coordinates(9,8), Coordinates(10,8), Coordinates(10,9), Coordinates(10,10), Coordinates(9,10)]
        actual = snake.draw(snakePositions)
        self.assertMultiLineEqual(expected, actual, "Expected:\n\n{0}\nActual:\n\n{1}".format(expected, actual))
        
    def testGenerateRandomHeadPosition(self):
        snake = Snake()
        headCoordinates1 = snake.generateRandomHeadCoordinates()
        headCoordinates2 = snake.generateRandomHeadCoordinates()
        self.assertNotEqual(headCoordinates1, headCoordinates2, "Coordinates shouldn't be equal!\nCoordinates 1: X:{0},Y:{1}\nCoordinates 2: X:{2},Y:{3}".format(headCoordinates1.x, headCoordinates1.y, headCoordinates2.x, headCoordinates2.y))
    
    def testGenerateRandomHeadPositionBorderFuzzTest(self):
        snake = Snake()
        coordinatesList = list()
        for i in range(100):
            coordinatesList.append(snake.generateRandomHeadCoordinates())
        xCoordinatesList = [coordinates.x for coordinates in coordinatesList]
        for x in xCoordinatesList:
            if x < 6:
                raise AssertionError("Generated x coordinate shouldn't be smaller than 5!!!")
    
    def testMoveSnakeUp(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        snake.move('U')
        actual = snake.getCoordinates()
        expectedCoordinates = [Coordinates(14,9), Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))
    
    def testMoveSnakeDown(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        snake.move('D')
        actual = snake.getCoordinates()
        expectedCoordinates = [Coordinates(14,11), Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))
    
    def testMoveSnakeRight(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        snake.move('R')
        actual = snake.getCoordinates()
        expectedCoordinates = [Coordinates(15,10), Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))
     
    def testMoveSnakeLeft(self):    
        snake = self.__setUpSnakeForMovingLeftRightUp()
        snake.move('L')
        actual = snake.getCoordinates()
        expectedCoordinates = [Coordinates(9,10), Coordinates(10,10), Coordinates(10,11), Coordinates(10,12), Coordinates(10,13)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))  
     
    def testMoveSnakeWrongInputRaises(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        self.assertRaises(DirectionError, snake.move, 'F')
     
    def testMoveSnakeLeftWrongDirectionRaises(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        self.assertRaises(DirectionError, snake.move, 'L')
 
    def testMoveSnakeDownWrongDirectionRaises(self):    
        snake = self.__setUpSnakeForMovingLeftRightUp()
        self.assertRaises(DirectionError, snake.move, 'D')

# Coordinate class tests:

    def testCoordinateEqualOverload(self):
        coord1 = Coordinates(0,3)
        coord2 = Coordinates(0,3)
        self.assertEquals(coord1 , coord2)

    def testCoordinateAddOverload(self):
        expected = Coordinates(0,3)
        actual = Coordinates(2,1) + Coordinates(-2,2)
        self.assertEquals(expected, actual, "Expected: {0},{1}\nActual: {2},{3}".format(expected.x, expected.y, actual.x, actual.y))

    def testCoordinatePrintOverload(self):
        coordinates = Coordinates(0,3)
        expected = "[x:0,y:3]"
        actual = coordinates.__str__()
        self.assertEquals(expected, actual, "Expected: {0}\nActual: {1}".format(expected , actual))

    def testCoordinateRepresentationOverload(self):
        coordinates = Coordinates(0,3)
        expected = "[x:0,y:3]"
        actual = coordinates.__repr__()
        self.assertEquals(expected, actual, "Expected: {0}\nActual: {1}".format(expected , actual))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()