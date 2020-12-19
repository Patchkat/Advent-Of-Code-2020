f = [int(x.rstrip('\n')) for x in open('xmas.txt').readlines()]
preamble_length = 25
for x in range(preamble_length, len(f)):
    current_nums = f[x-preamble_length:x]
    summed = False
    for y in current_nums:
        if (f[x] - y) in current_nums:
            summed = True
    if summed == False:
        print(f[x])
        break
