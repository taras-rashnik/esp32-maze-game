from ili934xnew import ILI9341, color565
from machine import I2C, Pin, SPI
import m5stack
import utime
from mpu6886 import MPU6886
# import glcdfont
# import tt14
# import tt24
# import tt32
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

power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
power.value(1)

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU6886(i2c)

renderer = MazeRenderer(maze)

# spi = SPI(
#     2,
#     baudrate=40000000,
#     miso=Pin(m5stack.TFT_MISO_PIN),
#     mosi=Pin(m5stack.TFT_MOSI_PIN),
#     sck=Pin(m5stack.TFT_CLK_PIN))

# display = ILI9341(
#     spi,
#     cs=Pin(m5stack.TFT_CS_PIN),
#     dc=Pin(m5stack.TFT_DC_PIN),
#     rst=Pin(m5stack.TFT_RST_PIN),
#     w=320,
#     h=240,
#     r=8)

# display.set_pos(0,0)
# display.fill_rectangle(0, 0, 320, 240, 0xffffff)

# hscale = 64
# vscale = 60

# for hwall in maze.horizontalWalls:
#     display.fill_rectangle(hscale * hwall.start.x - 5, vscale * hwall.start.y - 5, hscale * hwall.length, 10, color565(0xFF, 0xFF, 0x00))

# for vwall in maze.verticalWalls:
#     display.fill_rectangle(hscale * vwall.start.x - 5, vscale * vwall.start.y - 5, 10, vscale * vwall.length, color565(0x00, 0xFF, 0xFF))

# display.fill_rectangle(int(hscale * maze.ball.location.x - 5), int(vscale * maze.ball.location.y - 5), 10, 10, color565(0xFF, 0x00, 0xFF))

renderer.draw_maze()
while True:
    x, y, z = sensor.acceleration
    print(x, y)

    utime.sleep_ms(100)
    # display.fill_rectangle(int(hscale * maze.ball.location.x - 5), int(vscale * maze.ball.location.y - 5), 10, 10, 0xffffff)
    maze.ball.location.x -= 0.01 * x
    maze.ball.location.y += 0.01 * y
    print(maze.ball.location)
    # display.fill_rectangle(int(hscale * maze.ball.location.x - 5), int(vscale * maze.ball.location.y - 5), 10, 10, color565(0xFF, 0x00, 0xFF))

print('Maze game finished')