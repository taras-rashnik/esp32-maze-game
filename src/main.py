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
    print(x, y)

    utime.sleep_ms(100)
    # display.fill_rectangle(int(hscale * maze.ball.location.x - 5), int(vscale * maze.ball.location.y - 5), 10, 10, 0xffffff)
    renderer.erase_ball()
    maze.ball.location.x -= 0.01 * x
    maze.ball.location.y += 0.01 * y
    renderer.draw_ball()
    # display.fill_rectangle(int(hscale * maze.ball.location.x - 5), int(vscale * maze.ball.location.y - 5), 10, 10, color565(0xFF, 0x00, 0xFF))

print('Maze game finished')