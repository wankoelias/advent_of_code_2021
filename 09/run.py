import numpy as np
from itertools import product

with open("input.txt") as f:
    data_in = f.read().split("\n")
arr = np.array([[int(x) for x in d] for d in data_in])

ymax, xmax = arr.shape

visited_coords = set()
pools = list()


def coord(y, x):
    return f"{y}-{x}"


def get_adjacient(y, x):

    adjacient = list()

    adjacient += [(y, x - 1)] if x > 0 else []
    adjacient += [(y, x + 1)] if x < xmax - 1 else []
    adjacient += [(y - 1, x)] if y > 0 else []
    adjacient += [(y + 1, x)] if y < ymax - 1 else []

    return adjacient


def explore_pool(y, x, pool):
    n = arr[y, x]
    coordinate = coord(y, x)

    if n == 9:
        return set()

    if coordinate in visited_coords:
        return set()

    visited_coords.add(coordinate)

    pool.add(coordinate)

    for adj_y, adj_x in get_adjacient(y, x):
        pool.update(explore_pool(adj_y, adj_x, pool))

    return pool


for py, px in product(*map(range, arr.shape)):

    explored_pool = explore_pool(py, px, pool=set())

    if len(explored_pool) > 0:
        pools.append(explored_pool)


print(np.product(sorted([len(x) for x in pools])[-3:]))
