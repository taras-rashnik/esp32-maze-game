from machine import I2C, Pin
import m5stack
import utime
from mpu6886 import MPU6886
from maze import *
import maze_reader as reader
from maze_renderer import MazeRenderer


print('Maze game started')

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

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU6886(i2c)

renderer = MazeRenderer(maze)

renderer.draw_maze()
while True:
    x, y, z = sensor.acceleration
    # print(x, y)

    utime.sleep_ms(40)
    renderer.erase_ball()
    maze.ball.location.x -= 0.01 * x
    maze.ball.location.y += 0.01 * y
    renderer.draw_ball()

print('Maze game finished')