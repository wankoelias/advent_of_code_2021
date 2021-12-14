import numpy as np

with open("input.txt") as f:
    data_in = f.read().split("\n")

arr = np.array([[int(x) for x in d] for d in data_in])

clip = lambda value: 0 if value < 0 else value

# 1. increase
# 2. flash
# 3. increase adjacent (repeat)
# 4. reset flashed

nflashed = 0


def flash_and_increase(flashed):

    global nflashed

    for (y, x) in zip(*np.where(arr > 9)):
        window = arr[clip(y - 1) : y + 2, clip(x - 1) : x + 2]
        if not flashed[y, x]:
            window += 1
            flashed[y, x] = True
            nflashed += 1

    if np.any(np.any((arr > 9) & ~flashed)):
        flash_and_increase(flashed)


def step():

    global arr
    arr += 1
    flash_and_increase(np.zeros(shape=arr.shape, dtype=bool))
    arr[arr > 9] = 0


for i in range(100):
    step()
print(nflashed)
