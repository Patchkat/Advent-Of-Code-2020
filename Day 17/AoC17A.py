def active_neighbors(coord):
    total = 0
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            for z in range(coord[2] - 1, coord[2] + 2):
                if (x, y, z) in coords and (x, y, z) != coord:
                    total += 1
    return total

f = [x.rstrip('\n') for x in open('coords.txt').readlines()]
active = set({})

for y in range(len(f)):
    for x in range(len(f[0])):
        if f[y][x] == '#':
            active.add((x, -y, 0))
for loops in range(6):

    coords = list(active)
    x = [pos[0] for pos in coords]
    y = [pos[1] for pos in coords]
    z = [pos[2] for pos in coords]

    min_pos = (min(x)-1, min(y)-1, min(z)-1)
    max_pos = (max(x)+1, max(y)+1, max(z)+1)

    for coord in coords:
        if not 1 < active_neighbors(coord) < 4:
            active.remove(coord)
    for x in range(min_pos[0], max_pos[0]+1):
        for y in range(min_pos[1], max_pos[1]+1):
            for z in range(min_pos[2], max_pos[2]+1):
                point = (x, y, z)
                if active_neighbors(point) == 3:
                    active.add(point)
print(len(active))