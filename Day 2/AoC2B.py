f = [item.rstrip('\n').split(' ') for item in open('database.txt').readlines()]
total = [(x[2][int(x[0].split("-")[0])-1] == x[1].strip(":")) ^ (x[2][int(x[0].split("-")[0])-1] == x[1].strip(":")) for x in f]
print(total.count(True))