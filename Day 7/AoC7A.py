def get_bags(pairs, bag):
    possible = [bag]
    final = []
    while len(possible) != 0:
        current = possible.pop()
        for x in pairs.keys():
            for y in pairs.get(x):
                if current in y:
                    possible.append(x)
                    final.append(x)      
    return list(dict.fromkeys(final))


f = [x.rstrip('\n') for x in open('bags.txt').readlines()]
bags = {}
num_bags = {}
for x in f:
    first = True
    declarations = False
    a_key = ''
    a_value = ''
    for z, y in enumerate(x.split(" ")):
        if first:
            if y == "bags":
                first = False
                a_key = a_key.rstrip()
                bags[a_key] = []
            else:
                a_key += y + " "
        elif declarations:
            if y == "no":
                break
            if y not in ['bag.', 'bag,', 'bags.', 'bags,']:
                a_value += y + " "
            elif y in ['bag.', 'bag,', 'bags.', 'bags,']:
                temp = bags[a_key]
                temp.append(a_value.rstrip())
                a_value = ''
        elif y == "contain":
            declarations = True

print(len(get_bags(bags, "shiny gold")))