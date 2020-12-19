def num_of_seats(row, col, is_empty):
    total = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            temp_row = -2
            temp_col = -2
            pos_row = x+row
            pos_col = y+col
            while (temp_row != pos_row or pos_col != temp_col):
                temp_row = pos_row
                temp_col = pos_col
                if pos_row < len(f) and pos_row > -1:
                    if pos_col < len(f[0]) and pos_col > -1:
                        if is_empty:
                            if f[pos_row][pos_col] == '#':
                                total += 1
                            elif f[pos_row][pos_col] == '.':
                                pos_row += x
                                pos_col += y
                        else:
                            if x != 0 or y != 0:
                                if f[pos_row][pos_col] == '#':
                                    total += 1
                                elif f[pos_row][pos_col] == '.':
                                    pos_row += x
                                    pos_col += y

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
for x in open('input.txt').readlines():
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
                if num_of_seats(row, col, False) >= 5:
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
                if num_of_seats(row, col, False) >= 5:
                    next_step[row][col] = 'L'
                else:
                    next_step[row][col] = '#'
print(total_seats())