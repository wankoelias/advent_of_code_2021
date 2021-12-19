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
        self.x = x
        self.y = y

    def setxy(self, attr, value):
        dots[self.x][self.y] = None
        setattr(self, attr, value)
        dots[self.x][self.y] = self

    def fold(self, axis, fold_pos):
        if getattr(self, axis) > fold_pos:

            self.setxy(axis, fold_pos - (getattr(self, axis) - fold_pos))

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


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
