f = [x.rstrip('\n') for x in open('game.txt').readlines()]
visited_pos = []
acc = 0
pos = 0
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
    print(acc)