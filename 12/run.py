from collections import defaultdict, Counter

with open("test_input.txt") as f:
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

    blocked_small_caves = blocked - {"start", "end"}

    visited.add(node)
    path.append(node)

    double_visits = len(
        [
            k
            for k, v in Counter(path).items()
            if k.islower() and k not in ("start", "end") and v > 1
        ]
    )

    small_revisit = blocked_small_caves if double_visits == 0 else set()

    possible_next = (cave[node] - blocked).union(small_revisit & cave[node])

    for next_node in possible_next:
        find_paths(next_node, visited.copy(), path.copy())


find_paths("start")

print(len(all_paths))
