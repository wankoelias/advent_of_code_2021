import numpy as np
from itertools import product

with open("input.txt") as f:
    data_in = f.read().split("\n")
arr = np.array([[int(x) for x in d] for d in data_in])

risk_level = 0

ymax, xmax = arr.shape

for y, x in product(*map(range, arr.shape)):

    def clip(c):
        return 0 if c < 0 else c

    n = arr[y, x]

    adjacient = list()

    adjacient += [arr[y, x - 1]] if x > 0 else []
    adjacient += [arr[y, x + 1]] if x < xmax - 1 else []
    adjacient += [arr[y - 1, x]] if y > 0 else []
    adjacient += [arr[y + 1, x]] if y < ymax - 1 else []

    if min(adjacient) > n:
        risk_level += 1 + n

    # window = arr[clip(x - 1) : x + 2, clip(y - 1) : y + 2]

    # if len(window[window <= n]) == np.product(window.shape) - 1:
    #     risk_level += 1 + n

print(risk_level)
