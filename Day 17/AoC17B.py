def active_neighbors(coord):
    total = 0
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            for z in range(coord[2] - 1, coord[2] + 2):
                for w in range(coord[3] - 1, coord[3] + 2):
                    if (x, y, z, w) in coords and (x, y, z, w) != coord:
                        total += 1
    return total

def inactive_neighbors(coords):
    inactive = set()
    for coord in coords:
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                for z in range(coord[2] - 1, coord[2] + 2):
                    for w in range(coord[3] - 1, coord[3] + 2):
                        if (x, y, z, w) not in coords and (x, y, z, w) != coord:
                            inactive.add((x, y, z, w))
    return inactive

f = [x.rstrip('\n') for x in open('coords.txt').readlines()]
active = set({})

for y in range(len(f)):
    for x in range(len(f[0])):
        if f[y][x] == '#':
            active.add((x, -y, 0, 0))
for loops in range(6):

    coords = list(active)
    x = [pos[0] for pos in coords]
    y = [pos[1] for pos in coords]
    z = [pos[2] for pos in coords]
    w = [pos[3] for pos in coords]

    min_pos = (min(x)-1, min(y)-1, min(z)-1, min(w)-1)
    max_pos = (max(x)+1, max(y)+1, max(z)+1, max(w)+1)

    for coord in coords:
        if not 1 < active_neighbors(coord) < 4:
            active.remove(coord)
    inactive = inactive_neighbors(coords)
    for x in inactive:
        if active_neighbors(x) == 3:
            active.add(x)
print(len(active))