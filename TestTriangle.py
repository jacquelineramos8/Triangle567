"""
    Jacqueline Ramos
    567A HW 02a Assignment: The program below was given to us to fix/add tests for the classifyTriangle function in Triangle.py 
    I added comments to the tests I added and/or changed. 
"""

"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testRightTriangleC(self):
        # checks if a right triangle is input, but 'a' is actually the hypotenuse
        # this checks that no matter what order the side lengths are put in, a right triangle will be recognized
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testScaleneTriangle(self):
        # tests for a scalene triangle using all different side values
        self.assertEqual(classifyTriangle(3,5,7),'Scalene','3,5,7 is a Scalene triangle')
    
    def testIsoscelesTriangle(self):
        # tests for isosceles where the equal sides are input in any order 
        self.assertEqual(classifyTriangle(3,5,3),'Isosceles','3,5,3 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,5,3 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(5,3,3),'Isosceles','3,5,3 is an Isosceles triangle')
    
    def testUpperBound(self):
        # tests if any or all sides are over the 200 length limit
        self.assertEqual(classifyTriangle(201,205,208),'InvalidInput')
        self.assertEqual(classifyTriangle(100,150,201),'InvalidInput')
        self.assertEqual(classifyTriangle(100,201,150),'InvalidInput')
        self.assertEqual(classifyTriangle(201,100,150),'InvalidInput')
    
    def testLowerBound(self):
        # tests if any or all of the sides are 0 or negative
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')
        self.assertEqual(classifyTriangle(0,4,5),'InvalidInput')
        self.assertEqual(classifyTriangle(4,0,5),'InvalidInput')
        self.assertEqual(classifyTriangle(4,5,0),'InvalidInput')
        self.assertEqual(classifyTriangle(-3,4,5),'InvalidInput')
        self.assertEqual(classifyTriangle(3,-4,5),'InvalidInput')
        self.assertEqual(classifyTriangle(3,4,-5),'InvalidInput')
    
    def testInteger(self):
        # tests if any of the sides are invalid decimal inputs
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput')
        self.assertEqual(classifyTriangle(3,4.5,5),'InvalidInput')
        self.assertEqual(classifyTriangle(3,4,5.5),'InvalidInput')
    
    def testNotATriangle(self):
        # tests if the side lengths do not constitute a triangle, with side length input in any order
        self.assertEqual(classifyTriangle(3,5,8),'NotATriangle')
        self.assertEqual(classifyTriangle(5,3,8),'NotATriangle')
        self.assertEqual(classifyTriangle(8,5,3),'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

