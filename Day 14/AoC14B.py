def apply_mask(num, mask):
    mask = [c for c in mask]
    num = ''.join(['0' for x in range(36 - len(num))]) + num
    num = [c for c in num]
    for y, x in enumerate(mask):
        if x == "X" or x == '1':
            num[y] = mask[y]
    
    poss = []
    for x in range(len(num)):
        if num[x] == 'X' or num[x] == '1':
            num = num[x:]
            break

    for x in range(len(num)):
        if num[x] == 'X':
            poss.append(x)

    nums = []
    nums = create_numbers(num, poss, 0, nums)
    
    return [x for x in nums if x != None]

def create_numbers(numbers, positions, pos, nums):
    if pos == len(positions):
        return ''.join([c for c in numbers])
    for x in range(2):
        numbers[positions[pos]] = str(x)
        nums.append(create_numbers(numbers, positions, pos+1, nums))
    if pos == 0:
        return nums

f = [x.rstrip('\n').split(' ') for x in open('masks.txt').readlines()]
bits = {}
mask = ''
for x in f:
    if x[0] == 'mask':
        mask = x[2]
    else:
        masks = apply_mask(bin(int(int(x[0].split('[')[1][:-1]))).replace("0b",""), mask)
        for y in masks:
            bits[int(y, 2)] = int(x[2])

total = 0
for x in bits.values():
    if x != 0:
        total += x
print(total)