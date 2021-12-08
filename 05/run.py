from collections import defaultdict

pointlist = list()


class Point:
    def __init__(self):
        pointlist.append(self)

    crosses = 0


points = defaultdict(lambda: defaultdict(Point))



with open("input.txt") as f:
    data_in = f.read().split("\n")
    coords = [[eval(x) for x in d.split(" -> ")] for d in data_in]

for (x_start, y_start), (x_end, y_end) in coords:
    x_start, x_end = sorted((x_start, x_end))
    y_start, y_end = sorted((y_start, y_end))

    if x_start == x_end:
        for y in range(y_start, y_end + 1):
            points[x_start][y].crosses += 1


    if y_start == y_end:
        for x in range(x_start, x_end + 1):
            points[x][y_start].crosses += 1


print(len([x for x in pointlist if x.crosses > 1]))
