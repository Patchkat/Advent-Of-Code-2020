def num_of_seats(row, col, is_empty):
    total = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if row + x < len(f) and col + y < len(f[0]):
                if row + x >= 0 and col + y >= 0:
                    if is_empty:
                        if f[row+x][col+y] == '#':
                            return 1
                    else:
                        if x != 0 or y != 0:
                            if f[row+x][col+y] == '#':
                                total += 1 
    return total

def set_equal():
    for row, x in enumerate(next_step):
        test = []
        for y in x:
            test.append(y)
        f[row] = test
        
def total_seats():
    total = 0
    for x in f:
        for y in x:
            if y == '#':
                total += 1
    return total


f = []
next_step = []
for x in open('seats.txt').readlines():
    f.append([c for c in x.rstrip('\n')])

for x in f:
    test = []
    for y in x:
        test.append(y)
    next_step.append(test)

for row in range(len(f)):
        for col in range(len(f[0])):
            if f[row][col] == 'L':
                if num_of_seats(row, col, True) == 0:
                    next_step[row][col] = '#'
                else:
                    next_step[row][col] = 'L'
            elif f[row][col] == '#':
                if num_of_seats(row, col, False) >= 4:
                    next_step[row][col] = 'L'
                else:
                    next_step[row][col] = '#'
while (next_step != f):
    set_equal()
    for row in range(len(f)):
        for col in range(len(f[0])):
            if f[row][col] == 'L':
                if num_of_seats(row, col, True) == 0:
                    next_step[row][col] = '#'
                else:
                    next_step[row][col] = 'L'
            elif f[row][col] == '#':
                if num_of_seats(row, col, False) >= 4:
                    next_step[row][col] = 'L'
                else:
                    next_step[row][col] = '#'
print(total_seats())