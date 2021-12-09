from collections import defaultdict
import numpy as np

pointlist = list()


class Point:
    def __init__(self):
        pointlist.append(self)

    crosses = 0


def print_arr(a):
    a = a.astype(str)
    a[a == "0"] = "."

    for row in a.T:
        print("".join(row))


points = defaultdict(lambda: defaultdict(Point))

# arr = np.zeros(shape=(10, 10), dtype=int)

with open("input.txt") as f:
    data_in = f.read().split("\n")
    coords = [[eval(x) for x in d.split(" -> ")] for d in data_in]

for (x_start, y_start), (x_end, y_end) in coords:
    declining_x, declining_y = False, False

    if x_start > x_end:
        declining_x = True
        x_start, x_end = x_end, x_start

    if y_start > y_end:
        declining_y = True
        y_start, y_end = y_end, y_start

    if x_start == x_end:
        for y in range(y_start, y_end + 1):
            points[x_start][y].crosses += 1
            # arr[x_start, y] += 1

    elif y_start == y_end:
        for x in range(x_start, x_end + 1):
            points[x][y_start].crosses += 1
            # arr[x, y_start] += 1

    else:
        for x, y in zip(range(x_start, x_end + 1), range(y_start, y_end + 1)):
            if declining_x:
                x = x_end - x + x_start
            if declining_y:
                y = y_end - y + y_start

            points[x][y].crosses += 1
            # arr[x, y] += 1
        # print_arr(arr)


print(len([x for x in pointlist if x.crosses > 1]))

