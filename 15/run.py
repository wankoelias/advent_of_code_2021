from networkx import astar_path, grid_graph, DiGraph
import numpy as np
from itertools import product
from math import ceil

with open("input.txt") as f:
    arr = np.genfromtxt(f, delimiter=1, dtype=int)

full_shape = list(np.array(arr.shape) * 5)

G_grid = grid_graph(dim=full_shape)

G = DiGraph(directed=True)


def weight(y, x):

    max_y, max_x = arr.shape

    offset = ceil((y + 1) / max_y) - 1 + ceil((x + 1) / max_x) - 1

    weight = arr[y % max_y, x % max_x] + offset

    return weight if weight < 10 else weight % 10 + 1


for pos in product(*map(range, full_shape)):

    for other in list(G_grid[pos]):
        G.add_edge(pos, other, weight=weight(*other))

path = astar_path(G, (0, 0), tuple(map(lambda x: x - 1, full_shape)))

print(sum([weight(*p) for p in path[1:]]))
