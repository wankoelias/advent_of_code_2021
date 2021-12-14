from functools import reduce

with open("input.txt") as f:
    data_in = f.read().split("\n")

mapping = {
    "{": "}",
    "(": ")",
    "<": ">",
    "[": "]",
}

scores_closing = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

score_list = list()

for row in data_in:
    expected = list()
    broken = False
    for char in row:

        if char in mapping.keys():
            expected.append(mapping[char])
        elif len(expected) == 0:
            broken = True
            break
        elif char == expected[-1]:
            expected.pop()
        else:
            broken = True
            break

    if not broken:
        score_list.append(
            reduce(lambda a, b: a * 5 + b, [scores_closing[x] for x in expected[::-1]])
        )

print(sorted(score_list)[int(len(score_list) / 2)])
