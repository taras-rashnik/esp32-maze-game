import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={:.2f}, y={:.2f}".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return False


class Vector(Point):
    def __repr__(self):
        return "Vector(x={:.2f}, y={:.2f}".format(self.x, self.y)


class Wall:
    color = 0xffff00
    width = 0.2

    def __init__(self, startPoint, length):
        self.start = startPoint
        self.length = length


class HorizontalWall(Wall):
    @property
    def end(self):
        return Point(self.start.x + self.length, self.start.y)

    @property
    def bounding_rect(self):
        return (self.start.x - self.width/2, self.start.y - self.width/2, self.length + self.width, self.width)


class VerticalWall(Wall):
    @property
    def end(self):
        return Point(self.start.x, self.start.y + self.length)

    @property
    def bounding_rect(self):
        return (self.start.x - self.width/2, self.start.y - self.width/2, self.width, self.length + self.width)


class Ball:
    color = 0x0000ff

    def __init__(self, location, velocity, radius):
        self.location = location
        self.velocity = velocity
        self.radius = radius

    def __repr__(self):
        return "Ball(location={:.2f}, velocity={:.2f}, radius={:.2f}), color={}".format(self.location, self.velocity, self.radius, self.color)

    @property
    def bounding_rect(self):
        return (self.location.x - self.radius/2, self.location.y - self.radius/2, self.radius, self.radius)


class Maze:
    background_color = 0xffffff

    def __init__(self, horizontalWalls, verticalWalls, ball):
        self.horizontalWalls = horizontalWalls
        self.verticalWalls = verticalWalls
        self.ball = ball

    def accelerate(self, acc, elapsed):
        accx, accy, _ = acc
        self.ball.velocity.x -= 0.004 * accx * elapsed
        self.ball.velocity.y += 0.004 * accy * elapsed

        # rolling resistance force
        abs_velocity = math.sqrt(
            self.ball.velocity.x**2 + self.ball.velocity.y**2)
        velocity_direction_x = self.ball.velocity.x / abs_velocity
        velocity_direction_y = self.ball.velocity.y / abs_velocity
        self.ball.velocity.x -= 0.0003 * velocity_direction_x * elapsed
        self.ball.velocity.y -= 0.0003 * velocity_direction_y * elapsed

        self.ball.location.x += 0.001 * self.ball.velocity.x * elapsed
        self.ball.location.y += 0.001 * self.ball.velocity.y * elapsed

        for vwall in self.verticalWalls:
            self._vcollide(vwall, self.ball)

        for hwall in self.horizontalWalls:
            self._hcollide(hwall, self.ball)


    kr = 0.8

    @staticmethod
    def _vcollide(vwall, ball):
        if ball.location.y >= vwall.start.y and ball.location.y <= (vwall.start.y + vwall.length):
            # horizontal distance betweem centers of ball and vwall
            dist = ball.location.x - vwall.start.x
            # minimum distance betweem centers of ball and vwall
            delta = ball.radius + vwall.width/2
            # ball to the left from vwall and collide
            if dist < 0 and dist > -delta:
                # change velocity to opposite direction
                ball.velocity.x *= -Maze.kr
                # bounce back to not overlap
                ball.location.x = vwall.start.x - delta
            # ball to the right from vwall and collide
            elif dist >= 0 and dist < delta:
                # change velocity to opposite direction
                ball.velocity.x *= -Maze.kr
                # bounce back to not overlap
                ball.location.x = vwall.start.x + delta

    @staticmethod
    def _hcollide(hwall, ball):
        if ball.location.x >= hwall.start.x and ball.location.x <= (hwall.start.x + hwall.length):
            # vertical distance betweem centers of ball and hwall
            dist = ball.location.y - hwall.start.y
            # minimum distance betweem centers of ball and hwall
            delta = ball.radius + hwall.width/2
            # ball to the left from vwall and collide
            if dist < 0 and dist > -delta:
                # change velocity to opposite direction
                ball.velocity.y *= -Maze.kr
                # bounce back to not overlap
                ball.location.y = hwall.start.y - delta
            # ball to the right from vwall and collide
            elif dist >= 0 and dist < delta:
                # change velocity to opposite direction
                ball.velocity.y *= -Maze.kr
                # bounce back to not overlap
                ball.location.y = hwall.start.y + delta
