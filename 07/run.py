with open("input.txt") as f:
    positions = [int(x) for x in f.read().split(",")]


lowest = None

for target_position in range(0, max(positions)):
    fuel = 0

    for position in positions:
        steps = abs(target_position - position)
        fuel += (steps * (steps + 1)) / 2

    if lowest:
        if fuel < lowest:
            lowest = fuel
    else:
        lowest = fuel


print(lowest)
