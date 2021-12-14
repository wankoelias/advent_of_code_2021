from collections import defaultdict

with open("input.txt") as f:
    data_in = f.read().split("\n")

cave = defaultdict(lambda: set())

for line in data_in:
    a, b = line.split("-")
    cave[a].add(b)
    cave[b].add(a)

all_paths = list()


def find_paths(node, path=list()):

    if node == "end":
        path.append(node)
        all_paths.append(path)
        return

    blocked = {x for x in set(path) if x.islower()}

    blocked_small_caves = blocked - {"start", "end"}

    path.append(node)

    double_visits = len(
        {
            x
            for x in path
            if x.islower() and x not in ("start", "end") and path.count(x) > 1
        }
    )

    small_revisit = blocked_small_caves if double_visits == 0 else set()

    possible_next = (cave[node] - blocked).union(small_revisit & cave[node])

    for next_node in possible_next:
        find_paths(next_node, path.copy())


find_paths("start")

print(len(all_paths))
