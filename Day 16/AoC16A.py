f = [x.rstrip('\n') for x in open('tickets.txt').readlines()]
vals = {}
nearby = False
wrong = []
for x in f:
    if "or" in x:
        y = x.split(":")
        vals[y[0]] = [x.split('-') for x in y[1].lstrip().split(" or ")]
    elif nearby:
        for y in x.split(','):
            total = 0
            for z in vals.keys():
                current = vals.get(z)
                if int(y) in range(int(current[0][0]), int(current[0][1]) + 1) or int(y) in range(int(current[1][0]), int(current[1][1]) + 1):
                    total += 1
            if total == 0:
                wrong.append(int(y))
    if 'nearby' in x:
        nearby = True
print(sum(wrong))