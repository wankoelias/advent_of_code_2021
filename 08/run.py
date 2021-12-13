from collections import defaultdict
from itertools import product

with open("input.txt") as f:
    data_in = f.read().split("\n")

    signal_patterns, output_values = list(
        zip(*[[x.split() for x in d.split("|")] for d in data_in])
    )


mapping = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}


def solve_pattern(pattern_to_solve):
    possible_mapping = defaultdict(lambda: set())
    for p, digit in product(pattern_to_solve, mapping):
        if len(mapping[digit]) == len(p):
            possible_mapping[p].add(digit)

    def all_found():
        return all(len(v) == 1 for k, v in possible_mapping.items())

    while not all_found():
        for pattern, possible_digits in possible_mapping.items():
            if len(possible_digits) == 1:
                single_set = set(pattern)
                single_digit = next(iter(possible_digits))

                # all number the single number is contained in
                supersets = {
                    k for k, v in mapping.items() if mapping[single_digit].issubset(v)
                }

                # all patterns that do not contain the single digit set
                to_remove = {
                    x for x in possible_mapping if not single_set.issubset(set(x))
                }

                for p in to_remove:
                    possible_mapping[p] -= supersets

                subsets = {
                    k for k, v in mapping.items() if v.issubset(mapping[single_digit])
                }

                to_remove = {
                    x for x in possible_mapping if not set(x).issubset(single_set)
                }

                for p in to_remove:
                    possible_mapping[p] -= subsets

        # assign numbers with only one possibility to pattern
        for n in mapping:
            appears_in_pattern = set()
            for p, possible_digits in possible_mapping.items():
                if n in possible_digits:
                    appears_in_pattern.add(p)

            if len(appears_in_pattern) == 1:
                possible_mapping[appears_in_pattern.pop()] = {n}

    return {"".join(sorted(k)): v.pop() for k, v in possible_mapping.items()}


summed = 0
for pattern, output_value in zip(signal_patterns, output_values):
    solved_mapping = solve_pattern(pattern)
    summed += int(
        "".join([str(solved_mapping["".join(sorted(x))]) for x in output_value])
    )

print(summed)
