f = [x.rstrip('\n').split(' ') for x in open('database.txt').readlines()]
total = [int(x[0].split("-")[0]) <= x[2].count(x[1].strip(":")) <= int(x[0].split("-")[1]) for x in f]
print(total.count(True))