f = [x.rstrip('\n') for x in open('train.txt').readlines()]
vals = {}
positions = {}
nearby = False
your = False
ticket = []
wrong = []
tickets = []
for x in f:
    if "or" in x:
        y = x.split(":")
        vals[y[0]] = [x.split('-') for x in y[1].lstrip().split(" or ")]
    elif nearby:
        poggers = []
        for y in x.split(','):
            total = 0
            for z in vals.keys():
                current = vals.get(z)
                if int(y) in range(int(current[0][0]), int(current[0][1]) + 1) or int(y) in range(int(current[1][0]), int(current[1][1]) + 1):
                    total += 1
            if total != 0:
                poggers.append(int(y))
        if len(poggers) == len(x.split(',')):
            tickets.append(poggers)
    elif 'nearby' in x:
        nearby = True
    elif your:
        ticket = x.split(',')
        your = False
    elif 'your' in x:
        your = True

for x in range(len(tickets[0])):
    for z in vals.keys():
        total = 0
        current = vals.get(z)
        for y in range(len(tickets)):
            if int(tickets[y][x]) in range(int(current[0][0]), int(current[0][1]) + 1) or int(tickets[y][x]) in range(int(current[1][0]), int(current[1][1]) + 1):
                total += 1
        if total == len(tickets):
            if z not in positions.keys():
                positions[z] = [x]
            else:
                positions.get(z).append(x)

new_positions = {}
while len(new_positions.keys()) != len(positions.keys()):
    for x in positions.keys():
        current = positions.get(x)
        if len(current) == 1:
            current = current[0]
            for y in positions.keys():
                if current in positions.get(y):
                    positions.get(y).remove(current)
            new_positions[x] = current

total = 1
for x in new_positions.keys():
    if 'departure' in x:
        total *= int(ticket[int(new_positions.get(x))])

print(total)