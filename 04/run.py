import numpy as np
from more_itertools import windowed

with open("input.txt") as f:
    data_in = f.read().split("\n\n")

numbers = eval(data_in[0])

boards = [
    np.array([[x for x in map(int, x.split())] for x in d.split("\n")])
    for d in data_in[1:]
]

boards_won = set()

for nums in windowed(numbers, 5):

    for num in nums:

        for n_board, b in enumerate(boards):
            b[b == num] = -1

            for i in range(5):
                if np.all(b[:, i] == -1) or np.all(b[i, :] == -1):
                    boards_won.add(n_board)

                    if len(boards_won) == len(boards):
                        print(sum(b[b > 0]) * num)
                        1 / 0
