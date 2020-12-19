word = open('memory.txt').readline()
f = word.split(",")
occurences = {}
total = len(f)
for x in f:
    occurences[x] = f.index(x) + 1
last_val = f[-1]
f = f[-1]
for x in range(total-1, 29999999):
    if occurences.get(f) != (x + 1 and None):
        pos = occurences.get(f)
        f = str(x - pos + 1)
    else:
        f = '0'
    occurences[last_val] = x + 1
    last_val = f

print(f)