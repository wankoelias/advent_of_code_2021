import re

with open("input.txt") as f:
    data_in = f.readlines()


x, y = 0, 0

for command in data_in:
    direction, distance = re.match("(\w+) (\d+)", command).groups()
    distance = int(distance)
    
    if direction == "up":
        y -= distance
    elif direction == "down":
        y += distance
    elif direction == "forward":
        x += distance
    else:
        x -= distance
    
print(x*y)
 
# part 2

x, y, aim = 0, 0, 0

for command in data_in:
    direction, distance = re.match("(\w+) (\d+)", command).groups()
    distance = int(distance)
    
    if direction == "up":
        aim -= distance
    elif direction == "down":
        aim += distance
    elif direction == "forward":
        x += distance
        y += distance * aim

    
print(x*y)