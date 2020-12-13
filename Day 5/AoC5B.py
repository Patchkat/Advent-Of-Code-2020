tickets = []
seat = 0
for x in [x.rstrip('\n') for x in open('tickets.txt').readlines()]:
    row = 0
    column = 0
    rmaxV = 127
    rminV = 0
    cmaxV = 7
    cminV = 0
    for y in x:
        if y == "F":
            rmaxV = int((rmaxV + rminV) / 2)
        elif y == "B":
            rminV = int((rmaxV + rminV) / 2)
        elif y == "L":
            cmaxV = int((cmaxV + cminV) / 2)
        else:
            cminV = int((cmaxV + cminV) / 2)
    tickets.append(int((rmaxV * 8) + cmaxV))
tickets.sort()
print(tickets[651])
print(tickets[652])
print(tickets[653])
for x, y in enumerate(tickets):
    if x < len(tickets) - 1:
        if tickets[x+1] != tickets[x] + 1:
            seat = tickets[x]
            break
print(seat)