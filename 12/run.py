from collections import defaultdict

with open("input.txt") as f:
    data_in = f.read().split("\n")

cave = defaultdict(lambda: set())

for line in data_in:
    a, b = line.split("-")
    cave[a].add(b)
    cave[b].add(a)

all_paths = list()


def find_paths(node, visited=set(), path=list()):

    if node == "end":
        path.append(node)
        all_paths.append(path)
        return

    blocked = {x for x in visited if x.islower()}

    possible_next = cave[node] - blocked

    visited.add(node)
    path.append(node)

    for next_node in possible_next:
        find_paths(next_node, visited.copy(), path.copy())


find_paths("start")

print(len(all_paths))
