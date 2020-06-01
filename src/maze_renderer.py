from maze import *
from ili934xnew import ILI9341
from machine import Pin, SPI
import m5stack


class MazeRenderer:
    def __init__(self, maze):
        self.maze = maze
        self.display = MazeRenderer._create_display()
        self.hscale = 63
        self.vscale = 59

    @staticmethod
    def _create_display():
        spi = SPI(
            2,
            baudrate=40000000,
            miso=Pin(m5stack.TFT_MISO_PIN),
            mosi=Pin(m5stack.TFT_MOSI_PIN),
            sck=Pin(m5stack.TFT_CLK_PIN))

        display = ILI9341(
            spi,
            cs=Pin(m5stack.TFT_CS_PIN),
            dc=Pin(m5stack.TFT_DC_PIN),
            rst=Pin(m5stack.TFT_RST_PIN),
            w=320,
            h=240,
            r=8)

        power = Pin(m5stack.TFT_LED_PIN, Pin.OUT)
        power.value(1)

        return display

    def _draw_rect(self, rect, color):
        x, y, w, h = rect
        self.display.fill_rectangle(
            int(self.hscale * x),
            int(self.vscale * y),
            int(self.hscale * w),
            int(self.vscale * h),
            color)

    def _draw_walls(self, walls):
        for w in walls:
            self._draw_rect(w.bounding_rect, Wall.color)

    def draw_maze(self):
        self.display.fill_rectangle(0, 0, self.display.width, self.display.height, Maze.background_color)
        self._draw_walls(self.maze.horizontalWalls)
        self._draw_walls(self.maze.verticalWalls)
        self.draw_ball()

    def draw_ball(self):
        self._draw_rect(self.maze.ball.bounding_rect, Ball.color)

    def erase_ball(self):
        self._draw_rect(self.maze.ball.bounding_rect, Maze.background_color)
