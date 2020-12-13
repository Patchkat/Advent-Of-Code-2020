max_ticket = 0
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
    if int((rmaxV * 8) + cmaxV) > max_ticket:
        max_ticket = int((rmaxV * 8) + cmaxV)
print(max_ticket)