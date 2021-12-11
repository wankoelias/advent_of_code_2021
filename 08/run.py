with open("input.txt") as f:
    data_in = f.read().split("\n")

    signal_patterns, output_values = list(
        zip(*[[x.split() for x in d.split("|")] for d in data_in])
    )


unique_segment_numbers = 2, 4, 3, 7

print(
    len(
        [
            x
            for x in [e for s in output_values for e in s]
            if len(x) in unique_segment_numbers
        ]
    )
)
