def apply_mask(num, mask):
    num = ''.join(['0' for x in range(36 - len(num))]) + num
    num = [c for c in num]
    for y, x in enumerate(mask):
        if x != "X":
            num[y] = mask[y]
    return int(''.join(num), 2)


f = [x.rstrip('\n').split(' ') for x in open('masks.txt').readlines()]
bits = {}
mask = ''
for x in f:
    if x[0] == 'mask':
        mask = x[2]
    else:
        bits[int(x[0].split('[')[1][:-1])] = apply_mask(bin(int(x[2])).replace("0b",""), mask)

total = 0
for x in bits.values():
    if x != 0:
        total += x
print(total)