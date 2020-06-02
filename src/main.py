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
    accx, accy, _ = sensor.acceleration
    # print(x, y)

    utime.sleep_ms(40)

    renderer.erase_ball()

    end = utime.ticks_ms()
    elapsed = utime.ticks_diff(end, start)
    start = end

    maze.ball.velocity.x -= 0.0001 * accx * elapsed
    maze.ball.velocity.y += 0.0001 * accy * elapsed

    maze.ball.location.x += 0.001 * maze.ball.velocity.x * elapsed
    maze.ball.location.y += 0.001 * maze.ball.velocity.y * elapsed

    for vwall in maze.verticalWalls:
        vcollide(vwall, maze.ball)

    for hwall in maze.horizontalWalls:
        hcollide(hwall, maze.ball)

    renderer.draw_ball()

print('Maze game finished')
