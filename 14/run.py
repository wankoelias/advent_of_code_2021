from more_itertools import pairwise
from collections import Counter, defaultdict

with open("input.txt") as f:
    polymer, rules_input = f.read().split("\n\n")
rules = defaultdict(
    str, {k: v for k, v in map(lambda r: r.split(" -> "), rules_input.split("\n"))}
)

max_iteration = 10


def polymerize_pair(a, b, iteration=0, max_iteration=0, count=Counter()):

    if iteration == max_iteration:
        return count

    insertion = rules["{a}{b}".format(a=a, b=b)]

    if insertion:
        count[insertion] += 1

        count = polymerize_pair(a, insertion, iteration + 1, max_iteration, count)
        count = polymerize_pair(insertion, b, iteration + 1, max_iteration, count)
    return count


counter = Counter(polymer)

for a, b in pairwise(polymer):
    counter = polymerize_pair(a, b, max_iteration=max_iteration, count=counter)

print(max(counter.values()) - min(counter.values()))
