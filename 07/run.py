from itertools import product
from collections import defaultdict

with open("input.txt") as f:
    positions = [int(x) for x in f.read().split(",")]


lowest = None, None

for target_position in positions:
    fuel = 0

    for position in positions:
        fuel += abs(target_position - position)

    if lowest[0]:
        if fuel < lowest[1]:
            lowest = target_position, fuel
    else:
        lowest = target_position, fuel


print(lowest)
