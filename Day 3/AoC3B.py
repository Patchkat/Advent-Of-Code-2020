f = [x.rstrip('\n') for x in open('map.txt').readlines()]
rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]
trees = [0, 0, 0, 0, 0]
for slope in range(5):
    pos = [0, 0]
    while pos[0] < len(f):
        if f[pos[0]][pos[1] % len(f[0])] == '#':
            trees[slope] += 1
        pos[0] += downs[slope]
        pos[1] += rights[slope]
print(trees[0]*trees[1]*trees[2]*trees[3]*trees[4])