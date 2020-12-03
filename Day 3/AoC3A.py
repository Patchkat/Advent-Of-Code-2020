f = [x.rstrip('\n') for x in open('map.txt').readlines()]
pos = [0, 0]
right = 3
down = 1
trees = 0
while pos[0] < len(f):
    if f[pos[0]][pos[1] % len(f[0])] == '#':
        trees += 1
    pos[0] += down
    pos[1] += right
print(trees)