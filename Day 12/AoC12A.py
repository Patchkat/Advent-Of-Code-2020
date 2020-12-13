import math
position = [0, 0]
direction = 0
cardinals = {'N' : [0, 1], 'S' : [0, -1], 'E' : [1, 0], 'W' : [-1, 0]}
for x in open('navigation.txt').readlines():
    x = x.rstrip('\n')
    if x[:1] in cardinals.keys():
        position[0] += cardinals.get(x[:1])[0] * int(x[1:])
        position[1] += cardinals.get(x[:1])[1] * int(x[1:])
    else:
        if x[:1] == 'F':
            position[0] += math.cos(direction) * int(x[1:])
            position[1] += math.sin(direction) * int(x[1:])
        elif x[:1] == 'L':
            direction = math.degrees(direction)
            direction += int(x[1:])
            direction = math.radians(direction)
        else:
            direction = math.degrees(direction)
            direction -= int(x[1:])
            direction = math.radians(direction)

print(abs(position[0]) + abs(position[1]))