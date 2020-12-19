def get_bags(pairs, bag):
    possible = [bag]
    final = {}
    while len(possible) != 0:
        current = possible.pop()
        if current in pairs.keys():
            for x in pairs.get(current):
                possible.append(x[2:])
            final[current] = pairs.get(current)        
    return final

def get_total_bags(pairs, bag, total):
    for x in pairs.get(bag[2:]):
        total += get_total_bags(pairs, x, 0)
    return int(bag[:2]) + (int(bag[:2]) * total)
    


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

recursive_bags = get_bags(bags, "shiny gold")
print(recursive_bags)
total = 0
for x in recursive_bags.get("shiny gold"):
    total += get_total_bags(recursive_bags, x, 0)
print(total)
