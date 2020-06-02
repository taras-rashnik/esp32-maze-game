from maze import *
import display
import m5stack


class MazeRenderer:
    def __init__(self, maze):
        self.maze = maze
        self.tft = MazeRenderer._create_display()
        self.hscale = 63
        self.vscale = 59

    @staticmethod
    def _create_display():
        tft = display.TFT()
        # M5Stack:
        #tft.init(tft.M5STACK, width=240, height=320, rst_pin=33, backl_pin=32, miso=19, mosi=23, clk=18, cs=14, dc=27, bgr=True, backl_on=1, invrot=3)

        tft.init( 
            tft.M5STACK, 
            width=240, 
            height=320,
            mosi=m5stack.TFT_MOSI_PIN, 
            miso=m5stack.TFT_MISO_PIN, 
            clk=m5stack.TFT_CLK_PIN, 
            cs=m5stack.TFT_CS_PIN,
            rst_pin=m5stack.TFT_RST_PIN,
            dc=m5stack.TFT_DC_PIN,
            backl_pin=m5stack.TFT_LED_PIN, 
            backl_on=1, 
            bgr=True, 
            invrot=3,
            speed=40000000)

        tft.tft_select()

        return tft

    def _draw_rect(self, rect, color):
        x, y, w, h = rect
        self.tft.rect(
            int(self.hscale * x),
            int(self.vscale * y),
            int(self.hscale * w),
            int(self.vscale * h),
            color, 
            color)

    def _draw_walls(self, walls):
        for w in walls:
            self._draw_rect(w.bounding_rect, Wall.color)

    def draw_maze(self):
        width, height = self.tft.screensize()
        self._draw_rect((0, 0, width, height), Maze.background_color)
        self._draw_walls(self.maze.horizontalWalls)
        self._draw_walls(self.maze.verticalWalls)
        self.draw_ball()

    def draw_ball(self):
        self._draw_rect(self.maze.ball.bounding_rect, Ball.color)

    def erase_ball(self):
        self._draw_rect(self.maze.ball.bounding_rect, Maze.background_color)
