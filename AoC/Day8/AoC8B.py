f = [x.rstrip('\n') for x in open('game.txt').readlines()]
swaps = []
for x, y in enumerate(f):
    if y[:3] == 'nop' or y[:3] == 'jmp':
            swaps.append(x)
for x in swaps:
    visited_pos = []
    acc = 0
    pos = 0
    if f[x][:3] == 'jmp':
        f[x] = 'nop' + f[x][3:]
    else:
        f[x] = 'jmp' + f[x][3:]
    while pos not in visited_pos and pos < len(f):
        visited_pos.append(pos)
        value = f[pos]
        if value[:3] == "acc":
            if value[4] == "+":
                acc += int(value[5:])
                pos += 1
            else:
                acc -= int(value[5:])
                pos += 1
        elif value[:3] == "jmp":
            if value[4] == "+":
                pos += int(value[5:])
            else:
                pos -= int(value[5:])
        else:
            pos += 1
            continue
    if pos in visited_pos and pos < len(f):
        if f[x][:3] == 'jmp':
            f[x] = 'nop' + f[x][3:]
        else:
            f[x] = 'jmp' + f[x][3:]
    else:
        print(acc)
        break