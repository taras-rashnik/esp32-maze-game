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

start = utime.ticks_ms()

while True:
    acc = sensor.acceleration
    utime.sleep_ms(10)

    renderer.erase_ball()

    end = utime.ticks_ms()
    elapsed = utime.ticks_diff(end, start)
    start = end
    maze.accelerate(acc, elapsed)

    renderer.draw_ball()

    if maze.is_ball_out:
        renderer.print_game_over()
        print('Game over')
        break

print('Maze game finished')
