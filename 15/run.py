from networkx import astar_path, grid_graph, DiGraph
import numpy as np
from itertools import product

with open("input.txt") as f:
    arr = np.genfromtxt(f, delimiter=1, dtype=int)

G_grid = grid_graph(dim=list(arr.shape))

G = DiGraph(directed=True)

for pos in product(*map(range, arr.shape)):

    for other in list(G_grid[pos]):
        G.add_edge(pos, other, weight=arr[other])

path = astar_path(G, (0, 0), tuple(map(lambda x: x - 1, arr.shape)))

print(sum([arr[p] for p in path[1:]]))
