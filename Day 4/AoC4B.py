import re
nums = lambda x, y, z: 1 if y <= x <= z else 0
hcl = lambda x, y : 1 if re.search('^#([0-9]|[a-f]){6}', x.get(y)) != None else 0
ecl = lambda x, y : ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].count(x.get(y))
pid = lambda x, y : 1 if re.search('[0-9]{9}', x.get(y)) != None else 0
passport = {}
total = 0
f = [x for x in open('passports.txt').readlines()]
for x in f:
    if not x in ['\n']:
        for y in x.rstrip('\n').split(' '):
            passport[y.split(":")[0]] = y.split(":")[1]
    else:
        if passport.keys().__contains__('cid'):
            passport.pop('cid')
        if len(passport) == 7:
            correct = 0
            for x in passport.keys():
                if x == 'byr':
                        correct += nums(int(passport.get(x)), 1920, 2002)
                if x == 'iyr':
                        correct += nums(int(passport.get(x)), 2010, 2020)
                if x == 'eyr':
                        correct += nums(int(passport.get(x)), 2020, 2030)
                if x == 'hgt':
                    if passport.get(x)[-2:] == 'cm':
                            correct += nums(int(passport.get(x)[:-2]), 150, 193)
                    elif passport.get(x)[-2:] == 'in':
                            correct += nums(int(passport.get(x)[:-2]), 59, 76)
                if x == 'hcl':
                    correct += hcl(passport, x)
                if x == 'ecl':
                    correct += ecl(passport, x)
                if x == 'pid':
                        correct += pid(passport, x)
            if correct == 7:
                total += 1
        passport = {}
print(total)