from more_itertools import pairwise, windowed

with open("input.txt") as f:
    data_in = [x for x in map(int, f.readlines())]


def n_increasing(data):
    return sum(1 for x, y in pairwise(data) if y > x)


part_1 = n_increasing(data_in)
print(part_1)


part_2 = n_increasing(sum(x) for x in windowed(data_in, 3))
print(part_2)
