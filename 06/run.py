import re

with open("input.txt") as f:
    timers = [int(x) for x in re.findall("\d+", f.read())]

day = 0
last_day = 80

while day < last_day:

    new_timers = list()

    day += 1

    for timer in timers:
        timer -= 1

        if timer == -1:
            timer = 6
            new_timers.append(8)

        new_timers.append(timer)

    timers = new_timers


print(len(timers))
