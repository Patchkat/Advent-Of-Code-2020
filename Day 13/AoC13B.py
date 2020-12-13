import math
from functools import reduce
f = [x.rstrip('\n').split(',') for x in open('buses.txt').readlines()]
times = []
positions = []
total = 0
for y, x in enumerate(f[1]):
    if x != 'x':
        times.append(int(x))
        positions.append(y)
current = 0
for pos in range(1, len(times)):
    done = False
    while not done:
        total = 0
        for y in range(pos+1):
            if (current + positions[y]) % times[y] != 0:
                break
            else:
                total += 1
        if total == pos + 1:
            done = True
        else:
            current += reduce(lambda a,b: a*b // math.gcd(a,b), times[:pos])
print(current)