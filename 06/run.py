import re
from collections import Counter

with open("input.txt") as f:
    timers = Counter([int(x) for x in re.findall("\d+", f.read())])

day = 0
last_day = 256

while day < last_day:

    day += 1

    new_timers = Counter()

    for k, v in timers.items():
        new_timers[k - 1] = v
    timers = new_timers

    n_spawning = timers[-1]
    timers[-1] = 0

    timers[8] += n_spawning
    timers[6] += n_spawning

print(sum(timers.values()))
