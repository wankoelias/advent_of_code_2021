import re
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

with open("input.txt") as f:
    dot_input, fold_input = f.read().split("\n\n")

dots = defaultdict(lambda: defaultdict(lambda: None))
iterdots = lambda: (dots[x][y] for x in dots for y in dots[x] if dots[x][y])


class Dot:
    def __init__(self, x, y):
        dots[x][y] = self
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def setxy(self, attr, value):
        dots[self._x][self._y] = None
        setattr(self, attr, value)
        dots[self._x][self._y] = self

    @x.setter
    def x(self, value):
        self.setxy("_X", value)

    @y.setter
    def y(self, value):
        self.setxy("_y", value)

    def fold(self, axis, fold_pos):
        if getattr(self, axis) > fold_pos:

            self.setxy("_" + axis, fold_pos - (getattr(self, axis) - fold_pos))

    def __repr__(self):
        return f"Dot({self._x}, {self._y})"


for p in dot_input.split("\n"):
    Dot(*eval(p))


for f in fold_input.split("\n"):
    axis, pos = re.match("fold along ([x,y])=(\d+)", f).groups()
    pos = int(pos)

    for p in list(iterdots()):
        p.fold(axis, pos)

shape = list(map(lambda m: max(m) + 1, zip(*[(p.y, p.x) for p in iterdots()])))

arr = np.zeros(shape)
for d in iterdots():
    arr[d.y, d.x] = 1

plt.imshow(arr)
plt.show()


# print(len(list(iterdots())))
