from __builtin__ import list
import unittest

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

from production import coordinate
from production.boundaries_error import BoundariesError
from production.coordinate import Coordinates
from production.direction_error import DirectionError
from production.snake import Snake


FOOD_STARTING_NUMBER = 4

class Test(unittest.TestCase):
    
    def __setUpSnakeForMovingUpDownRight(self):
        snake = Snake()
        snake.setSnakeCoordinates([Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10), Coordinates(10,10)])
        return snake

    def __setUpSnakeForMovingLeftRightUp(self):
        snake = Snake()
        snake.setSnakeCoordinates([Coordinates(10,10), Coordinates(10,11), Coordinates(10,12), Coordinates(10,13), Coordinates(10,14)])
        return snake

    def __setUpSnakeForMovingUpLeftBorder(self):
        snake = Snake()
        snake.setSnakeCoordinates([Coordinates(1,1), Coordinates(1,2), Coordinates(1,3), Coordinates(1,4), Coordinates(1,5)])
        return snake

    def __setUpSnakeForMovingDownRightBorder(self):
        snake = Snake()
        snake.setSnakeCoordinates([Coordinates(20,20), Coordinates(20,19), Coordinates(20,18), Coordinates(20,17), Coordinates(20,16)])
        return snake

    def __setUpSnakeForMovingUpLeftBorderSafe(self):
        snake = Snake()
        snake.setSnakeCoordinates([Coordinates(2,2), Coordinates(2,3), Coordinates(2,4), Coordinates(2,5), Coordinates(2,6)])
        return snake

    def __setUpSnakeForMovingDownRightBorderSafe(self):
        snake = Snake()
        snake.setSnakeCoordinates([Coordinates(19,19), Coordinates(19,18), Coordinates(19,17), Coordinates(19,16), Coordinates(19,15)])
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
        actual = snake.draw(None, None)
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
        actual = snake.draw(snakePositions, None)
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
        actual = snake.draw(snakePositions, None)
        self.assertMultiLineEqual(expected, actual, "Expected:\n\n{0}\nActual:\n\n{1}".format(expected, actual))
        
        
    def testDrawFood(self):
        expected = """ -------------------- 
| *                  |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
| *   @@@@@        * |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                 *  |
|                    |
|                    |
 -------------------- """
        snake = Snake()
        snakePositions = [Coordinates(10,10), Coordinates(9,10), Coordinates(8,10), Coordinates(7,10), Coordinates(6,10)]
        foodPositions = [Coordinates(2,1), Coordinates(19,10), Coordinates(18,18), Coordinates(2,10)]
        actual = snake.draw(snakePositions, foodPositions)
        self.assertMultiLineEqual(expected, actual, "Expected:\n\n{0}\nActual:\n\n{1}".format(expected, actual))
        
    def testDrawOtherFood(self):
        expected = """ -------------------- 
|    *               |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|     @@@@@         *|
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
| *              *   |
|                    |
|                    |
 -------------------- """
        snake = Snake()
        snakePositions = [Coordinates(10,10), Coordinates(9,10), Coordinates(8,10), Coordinates(7,10), Coordinates(6,10)]
        foodPositions = [Coordinates(5,1), Coordinates(2,18), Coordinates(17,18), Coordinates(20,10)]
        actual = snake.draw(snakePositions, foodPositions)
        self.assertMultiLineEqual(expected, actual, "Expected:\n\n{0}\nActual:\n\n{1}".format(expected, actual))
        
    def testGenerateRandomHeadPosition(self):
        snake = Snake()
        headCoordinates1 = snake.generateRandomHeadCoordinates()
        headCoordinates2 = snake.generateRandomHeadCoordinates()
        self.assertNotEqual(headCoordinates1, headCoordinates2, "Coordinates shouldn't be equal!\nCoordinates 1: X:{0},Y:{1}\nCoordinates 2: X:{2},Y:{3}".format(headCoordinates1.x, headCoordinates1.y, headCoordinates2.x, headCoordinates2.y))
    
        
    def testGenerateRandomFoodPosition(self):
        snake = Snake()
        snake2 = Snake()
        snake.generateRandomFoodCoordinates(FOOD_STARTING_NUMBER)
        snake2.generateRandomFoodCoordinates(FOOD_STARTING_NUMBER)
        assert_that(snake.getFoodCoordinates(), not equal_to(snake2.getFoodCoordinates()))
            
    def testGenerateRandomHeadPositionBorderFuzzTest(self):
        for i in range(100):
            snake = Snake()
            if snake.generateRandomHeadCoordinates().x < 6:
                raise AssertionError("Generated x coordinate shouldn't be smaller than 5!!!")
            
    def testGenerateRandomFoodPositionOverSnakeFuzzTest(self):
        for i in range(100):
            snake = Snake()
            snakeCoordinatesList = snake.getSnakeCoordinates()
            snake.generateRandomFoodCoordinates(FOOD_STARTING_NUMBER)
            for foodCoordinates in snake.getFoodCoordinates():
                if foodCoordinates in snakeCoordinatesList:
                    raise AssertionError("Generated food coordinates shouldn't overlap snake!!!")
            
    def testGenerateRandomFoodPositionOverFoodPositionFuzzTest(self):
        for i in range(100):
            snake = Snake()
            snake.generateRandomFoodCoordinates(FOOD_STARTING_NUMBER)
            seen = list()
            for foodCoordinates in snake.getFoodCoordinates():
                if foodCoordinates in seen:
                    raise AssertionError("Generated food coordinates shouldn't overlap other food coordinates!!!")
                else:
                    seen.append(foodCoordinates)
            
    def testCreateNewFoodPositionOverFoodPositionFuzzTest(self):
        snake = Snake()
        for i in range(380):
            snake.generateRandomFoodCoordinates(1)
            seen = list()
            for foodCoordinates in snake.getFoodCoordinates():
                if foodCoordinates in seen:
                    raise AssertionError("Generated food coordinates shouldn't overlap other food coordinates!!!")
                else:
                    seen.append(foodCoordinates)
    
    def testMoveSnakeUp(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        snake.move('U')
        actual = snake.getSnakeCoordinates()
        expectedCoordinates = [Coordinates(14,9), Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))
    
    def testMoveSnakeDown(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        snake.move('D')
        actual = snake.getSnakeCoordinates()
        expectedCoordinates = [Coordinates(14,11), Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))
    
    def testMoveSnakeRight(self):    
        snake = self.__setUpSnakeForMovingUpDownRight()
        snake.move('R')
        actual = snake.getSnakeCoordinates()
        expectedCoordinates = [Coordinates(15,10), Coordinates(14,10), Coordinates(13,10), Coordinates(12,10), Coordinates(11,10)]
        self.assertListEqual(expectedCoordinates, actual, self.__formatExpectedActual(expectedCoordinates, actual))
     
    def testMoveSnakeLeft(self):    
        snake = self.__setUpSnakeForMovingLeftRightUp()
        snake.move('L')
        actual = snake.getSnakeCoordinates()
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
        
    def testSnakeBodyNoPelletNoGrowth(self):
        snake = self.__setUpSnakeForMovingLeftRightUp()
        snake.setFoodCoordinates([Coordinates(10,20), Coordinates(1,1), Coordinates(20,20), Coordinates(1,20)])
        snake.move('U')
        assert_that(len(snake.getSnakeCoordinates()), equal_to(5))
        
    def testSnakeBodyGrowth(self):
        snake = self.__setUpSnakeForMovingLeftRightUp()
        snake.setFoodCoordinates([Coordinates(10,9), Coordinates(1,1), Coordinates(20,20), Coordinates(1,20)])
        snake.move('U')
        assert_that(len(snake.getSnakeCoordinates()), equal_to(6))
        
    def testFoodPelletGenerationAfterSnakeEats(self):
        snake = self.__setUpSnakeForMovingLeftRightUp()
        snake.setFoodCoordinates([Coordinates(10,9), Coordinates(1,1), Coordinates(20,20), Coordinates(1,20)])
        snake.move('U')
        assert_that(len(snake.getFoodCoordinates()), equal_to(4) and Coordinates(10,9) not in snake.getFoodCoordinates())

    def testSnakeConstraintsUp(self):
        snake = self.__setUpSnakeForMovingUpLeftBorder()
        self.assertRaises(BoundariesError, snake.move, 'U')

    def testSnakeConstraintsLeft(self):
        snake = self.__setUpSnakeForMovingUpLeftBorder()
        self.assertRaises(BoundariesError, snake.move, 'L')

    def testSnakeConstraintsDown(self):
        snake = self.__setUpSnakeForMovingDownRightBorder()
        self.assertRaises(BoundariesError, snake.move, 'D')

    def testSnakeConstraintsRight(self):
        snake = self.__setUpSnakeForMovingDownRightBorder()
        self.assertRaises(BoundariesError, snake.move, 'R')

    def testSnakeConstraintsUpSafe(self):
        snake = self.__setUpSnakeForMovingUpLeftBorderSafe()
        snake.move('U')

    def testSnakeConstraintsLeftSafe(self):
        snake = self.__setUpSnakeForMovingUpLeftBorderSafe()
        snake.move('L')

    def testSnakeConstraintsDownSafe(self):
        snake = self.__setUpSnakeForMovingDownRightBorderSafe()
        snake.move('D')

    def testSnakeConstraintsRightSafe(self):
        snake = self.__setUpSnakeForMovingDownRightBorderSafe()
        snake.move('R')
            
# Coordinate class tests:

    def testCoordinateEqualOverload(self):
        coord1 = Coordinates(0,3)
        coord2 = Coordinates(0,3)
        self.assertEquals(coord1 , coord2)

    def testCoordinateNotEqualOverloadReturnFalse(self):
        coord1 = Coordinates(0,3)
        coord2 = Coordinates(0,3)
        assert_that(coord1 != coord2, equal_to(False))

    def testCoordinateNotEqualOverloadReturnTrue(self):
        coord1 = Coordinates(0,3)
        coord2 = Coordinates(2,3)
        assert_that(coord1 != coord2, equal_to(True))
        
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