f = [int(x.rstrip('\n')) for x in open('adapters.txt').readlines()]
f.sort()
f.insert(0, 0)
num_of_ones = 0
num_of_threes = 1
for x in range(len(f) - 1):
    if f[x+1] - f[x] == 1:
        num_of_ones += 1
    elif f[x+1] - f[x] == 3:
        num_of_threes += 1
print(num_of_ones * num_of_threes)