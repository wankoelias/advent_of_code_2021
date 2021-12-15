from collections import defaultdict

cave = defaultdict(lambda: set())

with open("input.txt") as f:

    for line in f:
        a, b = line.rstrip().split("-")
        cave[a].add(b)
        cave[b].add(a)

n_paths = 0


def find_paths(node, path=list()):

    if node == "end":
        global n_paths
        n_paths += 1
        return

    blocked = {x for x in set(path) if x.islower()}

    blocked_small_caves = blocked - {"start"}

    path.append(node)

    small_cave_revisits = len({x for x in blocked_small_caves if path.count(x) > 1})

    small_caves_to_revisit = blocked_small_caves if small_cave_revisits == 0 else set()

    possible_next = (cave[node] - blocked).union(small_caves_to_revisit & cave[node])

    for next_node in possible_next:
        find_paths(next_node, path.copy())


find_paths("start")

print(n_paths)
