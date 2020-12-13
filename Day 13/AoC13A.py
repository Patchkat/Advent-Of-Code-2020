f = [x.rstrip('\n').split(',') for x in open('buses.txt').readlines()]
time = int(f[0][0])
times = []
beg_times = []
for x in f[1]:
    if x != 'x':
        times.append(int(x))
        beg_times.append(int(x))
total = 1
while max(times) < time:
    times[times.index(max(times))] += beg_times[times.index(max(times))]
    total += 1
times = [x * total for x in beg_times]
closest = max(times)
pos = 0
for y, x in enumerate(times):
    if time < x <= closest:
        closest = x 
        pos = y
print((closest - time) * beg_times[pos])