import math
position = [0, 0]
waypoint = [10, 1]
cardinals = {'N' : [0, 1], 'S' : [0, -1], 'E' : [1, 0], 'W' : [-1, 0]}
for x in open('navigation.txt').readlines():
    x = x.rstrip('\n')
    if x[:1] in cardinals.keys():
        waypoint[0] += cardinals.get(x[:1])[0] * int(x[1:])
        waypoint[1] += cardinals.get(x[:1])[1] * int(x[1:])
    else:
        if x[:1] == 'F':
            position[0] += waypoint[0] * int(x[1:])
            position[1] += waypoint[1] * int(x[1:])
        elif x[:1] == 'L' or x[:1] == 'R':
            if int(x[1:]) == 90:
                if x[:1] == 'L':
                    temp = waypoint[0]
                    waypoint[0] = -waypoint[1]
                    waypoint[1] =  temp
                else:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] =  -temp
            elif int(x[1:]) == 180:
                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]
            elif int(x[1:]) == 270:
                if x[:1] == 'L':
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] =  -temp
                else:
                    temp = waypoint[0]
                    waypoint[0] = -waypoint[1]
                    waypoint[1] =  temp
                
            

print(abs(position[0]) + abs(position[1]))