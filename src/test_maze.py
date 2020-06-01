import unittest
from maze import *


class TestPoint(unittest.TestCase):

    def test_constructor(self):
        point = Point(10, 15)
        self.assertIsNotNone(point)

    def test_repr(self):
        point = Point(10, 15.6)
        s = repr(point)
        self.assertEqual(s, "Point(x=10.00, y=15.60")


class TestVector(unittest.TestCase):

    def test_constructor(self):
        vector = Vector(10, 15)
        self.assertIsNotNone(vector)

    def test_repr(self):
        vector = Vector(10, 15.6)
        s = repr(vector)
        self.assertEqual(s, "Vector(x=10.00, y=15.60")


class TestWall(unittest.TestCase):

    def test_constructor(self):
        horizontalWall = HorizontalWall(Point(1, 1), 5)
        self.assertIsNotNone(horizontalWall)
        self.assertEqual(Point(6, 1), horizontalWall.end)

        verticalWall = VerticalWall(Point(1, 1), 5)
        self.assertIsNotNone(verticalWall)
        self.assertEqual(Point(1, 6), verticalWall.end)

    def test_bounding_rect(self):
        Wall.width = 0.8

        hwall = HorizontalWall(Point(2.3, 23.8), 12.1)
        self.assertEqual(hwall.bounding_rect, (2.3-0.8/2, 23.8-0.8/2, 12.1+0.8, 0.8))

        vwall = VerticalWall(Point(5.3, 14.8), 34.1)
        self.assertEqual(vwall.bounding_rect, (5.3-0.8/2, 14.8-0.8/2, 0.8, 34.1+0.8))


class TestMaze(unittest.TestCase):

    def test_constructor(self):
        maze = Maze(1, 1, 1)
        self.assertIsNotNone(maze)


if __name__ == "__main__":
    unittest.main()
