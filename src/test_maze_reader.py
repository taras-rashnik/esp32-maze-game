import unittest
from maze import *
import maze_reader as reader


class TestMazeReader(unittest.TestCase):

    def test_walls_from_horizontal_line(self):
        walls = reader.walls_from_horizontal_line('+-+-+-+-+-+', 6)
        self.assertEqual(len(walls), 1)
        self.assertEqual(walls[0].start, Point(0, 6))
        self.assertEqual(walls[0].length, 5)

        walls = reader.walls_from_horizontal_line('+-+-+ +-+-+', 7)
        self.assertEqual(len(walls), 2)
        self.assertEqual(walls[0].start, Point(0, 7))
        self.assertEqual(walls[0].length, 2)
        self.assertEqual(walls[1].start, Point(3, 7))
        self.assertEqual(walls[1].length, 2)

        walls = reader.walls_from_horizontal_line('+ +-+ +-+ +', 8)
        self.assertEqual(len(walls), 2)
        self.assertEqual(walls[0].start, Point(1, 8))
        self.assertEqual(walls[0].length, 1)
        self.assertEqual(walls[1].start, Point(3, 8))
        self.assertEqual(walls[1].length, 1)

    def test_walls_from_vertical_line(self):
        walls = reader.walls_from_vertical_line('+|+|+|+|+', 6)
        self.assertEqual(len(walls), 1)
        self.assertEqual(walls[0].start, Point(6, 0))
        self.assertEqual(walls[0].length, 4)

        walls = reader.walls_from_vertical_line('+|+|+ +|+', 7)
        self.assertEqual(len(walls), 2)
        self.assertEqual(walls[0].start, Point(7, 0))
        self.assertEqual(walls[0].length, 2)
        self.assertEqual(walls[1].start, Point(7, 3))
        self.assertEqual(walls[1].length, 1)

    def test_get_vertical_line(self):
        lines = [
            '+-+-+-+-+-+',
            '|.|. . . .|',
            '+ + + + + +',
            '|.|.|.|.|.|',
            '+ + + + +-+',
            '|. .|.|. .]',
            '+ +-+ +-+ +',
            '|.|. . .|.|',
            '+-+-+-+-+-+'
        ]

        self.assertEqual('+|+|+|+|+', reader.get_vertical_line(lines, 0))
        self.assertEqual('+|+|+ +|+', reader.get_vertical_line(lines, 2))
        self.assertEqual('+ +|+|+ +', reader.get_vertical_line(lines, 4))
        self.assertEqual('+|+|+]+|+', reader.get_vertical_line(lines, 10))

    def test_find_ball_location(self):
        lines = [
            '+-+-+-+-+-+',
            '|.|. . . .|',
            '+ + + + + +',
            '|.|.|.|.|.|',
            '+ + + + +-+',
            '|. .|.|. .]',
            '+ +-+ +-+ +',
            '|.|. . o|.|',
            '+-+-+-+-+-+'
        ]

        self.assertEqual(Point(3.5, 3.5), reader.find_ball_location(lines))
        self.assertEqual(Point(5, 2), reader.find_exit_wall(lines).start)

        lines = [
            '+-+-+-+-+-+',
            '|.|. . . o]',
            '+ + + + + +',
            '|.|.|.|.|.|',
            '+ + + + +-+',
            '|. .|.|. .|',
            '+ +-+ +-+ +',
            '|.|. . .|.|',
            '+-+-+-+-+-+'
        ]

        self.assertEqual(Point(4.5, 0.5), reader.find_ball_location(lines))
        self.assertEqual(Point(5, 0), reader.find_exit_wall(lines).start)

        lines = [
            '+-+-+-+-+-+',
            '|.|. . . .|',
            '+ + + + + +',
            '|.|.|.|.|.|',
            '+ + + + +-+',
            '|. .|.|. .|',
            '+ +-+ +-+ +',
            '|o|. . .|.]',
            '+-+-+-+-+-+'
        ]

        self.assertEqual(Point(0.5, 3.5), reader.find_ball_location(lines))
        self.assertEqual(Point(5, 3), reader.find_exit_wall(lines).start)

    def test_simple_walls(self):
        s = """
            +-+
            |.|
            +-+
        """
        maze = reader.maze_from_string(s)
        self.assertEqual(2, len(maze.horizontalWalls))
        self.assertEqual(2, len(maze.verticalWalls))

        self.assertEqual(Point(0, 0), maze.horizontalWalls[0].start)
        self.assertEqual(1, maze.horizontalWalls[0].length)

        self.assertEqual(Point(0, 1), maze.horizontalWalls[1].start)
        self.assertEqual(1, maze.horizontalWalls[1].length)

        self.assertEqual(Point(0, 0), maze.verticalWalls[0].start)
        self.assertEqual(1, maze.verticalWalls[0].length)

        self.assertEqual(Point(1, 0), maze.verticalWalls[1].start)
        self.assertEqual(1, maze.verticalWalls[1].length)

    def test_simple_walls2(self):
        s = """
            +-+-+
            |. .|
            + + +
            |. .|
            +-+-+
        """
        maze = reader.maze_from_string(s)
        self.assertEqual(2, len(maze.horizontalWalls))
        self.assertEqual(2, len(maze.verticalWalls))

        self.assertEqual(Point(0, 0), maze.horizontalWalls[0].start)
        self.assertEqual(2, maze.horizontalWalls[0].length)

        self.assertEqual(Point(0, 2), maze.horizontalWalls[1].start)
        self.assertEqual(2, maze.horizontalWalls[1].length)

        self.assertEqual(Point(0, 0), maze.verticalWalls[0].start)
        self.assertEqual(2, maze.verticalWalls[0].length)

        self.assertEqual(Point(2, 0), maze.verticalWalls[1].start)
        self.assertEqual(2, maze.verticalWalls[1].length)

    def test_simple_walls3(self):
        s = """
            +-+-+-+-+-+
            |.|. . . .|
            + + + + + +
            |.|.|.|.|.|
            + + + + +-+
            |. o|.|. .]
            + +-+ +-+ +
            |.|. . .|.|
            +-+-+-+-+-+
        """
        maze = reader.maze_from_string(s)
        self.assertEqual(5, len(maze.horizontalWalls))
        self.assertEqual(9, len(maze.verticalWalls))

        self.assertEqual(maze.ball.location, Point(1.5, 2.5))


if __name__ == "__main__":
    unittest.main()
