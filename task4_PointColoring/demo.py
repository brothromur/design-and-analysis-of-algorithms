from point_coloring import *


def is_balanced(points, colors):
    # on every horizontal and vertical line, black and white counts differ by at most 1
    for axis in (0, 1):
        lines = {}
        for k, p in enumerate(points):
            lines.setdefault(p[axis], []).append(colors[k])
        for line in lines.values():
            if abs(line.count('B') - line.count('W')) > 1:
                return False
    return True


RECTANGLE = [(0, 0), (2, 0), (2, 1), (0, 1)]                 # a cycle
LINE = [(0, 0), (1, 0), (2, 0)]                              # a path plus a leftover point
SIXTEEN = [(0, 0), (1, 0), (4, 0), (6, 0),
           (0, 1), (2, 1), (3, 1), (5, 1),
           (1, 2), (3, 2), (5, 2), (6, 2),
           (1, 3), (2, 3), (4, 3), (6, 3)]                   # one long path


def test_rectangle():
    colors = point_coloring(len(RECTANGLE), RECTANGLE)
    assert colors == ['B', 'W', 'B', 'W'] and is_balanced(RECTANGLE, colors)


def test_line():
    colors = point_coloring(len(LINE), LINE)
    assert colors == ['B', 'W', 'B'] and is_balanced(LINE, colors)


def test_sixteen():
    colors = point_coloring(len(SIXTEEN), SIXTEEN)
    assert is_balanced(SIXTEEN, colors)
    assert colors[12] != colors[15]          # the two ends of a path get opposite colors


print("Rectangle:", point_coloring(len(RECTANGLE), RECTANGLE))
print("Line:", point_coloring(len(LINE), LINE))
print("16 points:", point_coloring(len(SIXTEEN), SIXTEEN))