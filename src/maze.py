
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

