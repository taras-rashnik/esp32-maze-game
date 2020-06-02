from maze import *


def walls_from_horizontal_line(line, idx):
    ystart = idx
    xstart = 0
    lenght = 0

    walls = []
    for i, c in enumerate([ch for ch in line if ch != '+']):
        if c == '-':
            lenght += 1
        else:
            if lenght > 0:
                walls.append(HorizontalWall(Point(xstart-Wall.width/2, ystart), lenght+Wall.width))
            xstart = i+1
            lenght = 0

    if lenght > 0:
        walls.append(HorizontalWall(Point(xstart-Wall.width/2, ystart), lenght+Wall.width))

    return walls


def walls_from_vertical_line(line, idx):
    xstart = idx
    ystart = 0
    lenght = 0

    walls = []
    for i, c in enumerate([ch for ch in line if ch != '+']):
        if c == '|':
            lenght += 1
        else:
            if lenght > 0:
                walls.append(VerticalWall(Point(xstart, ystart-Wall.width/2), lenght+Wall.width))
            ystart = i+1
            lenght = 0

    if lenght > 0:
        walls.append(VerticalWall(Point(xstart, ystart-Wall.width/2), lenght+Wall.width))

    return walls


def get_vertical_line(lines, idx):
    chrs = [l[idx] for l in lines]
    return ''.join(chrs)


def find_ball_location(lines):
    for i, l in enumerate(lines):
        j = l.find('o')
        if j >= 0:
            return Point(j/2, i/2)

    return Point(0.5, 0.5)


def find_exit_wall(lines):
    for i, l in enumerate(lines):
        j = l.find(']')
        if j >= 0:
            return VerticalWall(Point(j//2, i//2), 1)

    return VerticalWall(Point(0, 0), 1)


def maze_from_string(s):
    lines = [l for l in map(str.strip, s.split("\n")) if len(l) >= 3]
    # print(lines)

    # minimum 3 lines
    if len(lines) < 3:
        raise ValueError(
            "Maze must consists of minimum 3 lines (eache line 3 char minimum).")

    # number of lines is odd
    if len(lines) % 2 != 1:
        raise ValueError("Maze must consists of odd number of lines.")

    # all lines have the same length
    len0 = len(lines[0])
    if not all(len0 == len(l) for l in lines):
        raise ValueError("All lines must have the same length.")

    hWalls = []
    vWalls = []

    # horizontal
    hlines = [hline for hline in lines if hline.startswith('+')]
    for i, hline in enumerate(hlines):
        hWalls += walls_from_horizontal_line(hline, i)

    # vertical
    vlines = [get_vertical_line(lines, i)
              for i in range(len0) if lines[0][i] == '+']
    for i, vline in enumerate(vlines):
        vWalls += walls_from_vertical_line(vline, i)

    # ball
    ball = Ball(find_ball_location(lines), Vector(0, 0), 0.2)

    return Maze(hWalls, vWalls, ball)
