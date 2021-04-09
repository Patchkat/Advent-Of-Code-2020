def find_corners(tiles_dict):
    corners = []
    pos = 0
    while pos < len(tiles_dict.keys()):
        x = list(tiles_dict.keys())[pos]
        total = 0
        for y in tiles_dict.keys():
            if x != y:
                if memoized(x, y):
                    total += 1
        if total == 2:
            corners.append(x)
        pos += 1
    return corners

def check_squares(t1, t2):
    squares = [t1, t2]
    total = 0
    for x in range(2):
        for y in range(4):
            for z in range(2):
                for rot in range(4):
                    if z == 1:
                        for line, s in enumerate(squares[0]):
                            squares[0].append(squares[0][9-line])
                            squares[0].pop(9-line)
                    e1 = get_edge(squares[0], len(squares[0]) - 1)
                    e2 = get_edge(squares[1], 0)
                    if e1 == e2:
                        return True
                    if z == 1:
                        for line, s in enumerate(squares[0]):
                            squares[0].append(squares[0][9-line])
                            squares[0].pop(9-line)
                    squares[1] = rotate(squares[1])
            squares[0] = rotate(squares[0])
        temp = [c for c in [d for d in squares[0]]]
        squares[0] = [c for c in [d for d in squares[1]]]
        squares[1] = temp
    return False

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
        result = check_squares(t1, t2)
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
x = 0
corners = find_corners(tiles_dict)
total = 1
for c in corners:
    total *= c
print(corners)
print(total)