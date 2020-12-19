f = [int(x.rstrip('\n')) for x in open('xmas.txt').readlines()]
nums = []
for x in range(len(f)):
    for y in range(len(f)):
        nums = f[x:x+y]
        if sum(nums) == 1639024365:
            print(max(nums) + min(nums))
            break