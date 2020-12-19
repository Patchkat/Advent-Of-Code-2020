word = open('memory.txt').readline()
f = word.split(",")
for x in range(len(f)-1, 2019):
    current = f[x]
    if f.count(current) != 1:
        f = f[::-1]
        pos = len(f) - f[1:].index(current) - 2
        f = f[::-1]
        f.append(str(x - pos)) 
    else:
        f.append('0')
print(f[-1])