import numpy as np
from collections import Counter

with open("input.txt") as f:
    data_in = f.read().split("\n")
arr = np.array([[int(x) for x in y] for y in data_in], dtype=bool)

rows, cols = arr.shape

gamma_list = ["1" if sum(arr[:, x]) > rows / 2 else "0" for x in range(cols)]

gamma = int("".join(gamma_list), 2)
epsilon = int("".join(["0" if x == "1" else "1" for x in gamma_list]), 2)

print(gamma * epsilon)


def bit_criteria(arr, search_for, bit=0):

    if arr.shape[0] == 1:
        return arr

    n_half = arr.shape[0] / 2.0
    n_True = sum(arr[:, bit])

    if search_for == 1:
        if n_True >= n_half:
            mask_value = 1
        else:
            mask_value = 0
    else:
        if n_True < n_half:
            mask_value = 1
        else:
            mask_value = 0

    mask = arr[:, bit] == mask_value

    return bit_criteria(arr[mask], search_for, bit + 1)


def to_int(a):
    return int("".join([str(x) for x in a.astype(int)[0]]), 2)


oxygen_rating = bit_criteria(arr, 1)
scrubber = bit_criteria(arr, 0)

print(to_int(oxygen_rating) * to_int(scrubber))
