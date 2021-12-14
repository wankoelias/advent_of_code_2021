with open("input.txt") as f:
    data_in = f.read().split("\n")

mapping = {
    "{": "}",
    "(": ")",
    "<": ">",
    "[": "]",
}

scores = {
    "}": 1197,
    ")": 3,
    ">": 25137,
    "]": 57,
}

score = 0

for row in data_in:
    expected = list()
    for i, char in enumerate(row):

        if char in mapping.keys():
            expected.append(mapping[char])
        elif len(expected) == 0:
            score += scores[char]
            break
        elif char == expected[-1]:
            expected.pop()
        else:
            score += scores[char]
            break

print(score)
