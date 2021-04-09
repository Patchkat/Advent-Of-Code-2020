def check_square(t1, t2):
    for y in range(4):
        for z in range(2):
            for rot in range(4):
                if z == 1:
                    for line, s in enumerate(t1):
                        t1.append(t1[9-line])
                        t1.pop(9-line)
                e1 = get_edge(t1, len(t1) - 1)
                e2 = get_edge(t2, 0)
                if e1 == e2:
                    return t1
                if z == 1:
                    for line, s in enumerate(t1):
                        t1.append(t1[9-line])
                        t1.pop(9-line)
                t2 = rotate(t2)
        t1 = rotate(t1)
    return None

def get_edge(square, side):
    edge = []
    for x in range(len(square)):
        edge.append(square[x][side])
    return edge
    
def rotate(square):
    longways = [[d for d in c] for c in square]
    for x in range(len(square)):
        for y in range(len(square)):
            square[y][9-x] = longways[x][y]
    return square

def memoized(pos1, pos2):
    if (pos1, pos2) in memoized_combos.keys():
        return memoized_combos[(pos1, pos2)]
    else: 
        t1 = tiles_dict.get(pos1)
        t2 = tiles_dict.get(pos2)
        result = check_square(t1, t2)
        memoized_combos[(pos1, pos2)] = result
        return result

f = open('input.txt').read().strip()
tiles_dict = {}
tiles = f.split('\n\n')
memoized_combos = {}
tiles = [c.split('\n') for c in tiles]
for tile in tiles:
    temp_tile = tile[1:]
    for pos, x in enumerate(temp_tile):
        tile[pos+1] = [c for c in x]
    tiles_dict[int(tile[0][5:].rstrip(':'))] = tile[1:]

total = 0
for x in tiles_dict.keys():
    x = tiles_dict.get(x)
    for y in x:
        for z in y:
            if z == '#':
                total += 1
print(total - (15 * int(input("Dragons: "))))