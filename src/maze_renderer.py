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

        return display

    def _draw_walls(self, walls):
        color = Wall.color
        for w in walls:
            x, y, w, h = w.bounding_rect
            self.display.fill_rectangle(
                int(self.hscale * x), 
                int(self.vscale * y), 
                int(self.hscale * w), 
                int(self.vscale * h), 
                color)

    def draw_maze(self):
        self._draw_walls(self.maze.horizontalWalls)
        self._draw_walls(self.maze.verticalWalls)

    def draw_ball(self):
        pass

    def erase_ball(self):
        pass
