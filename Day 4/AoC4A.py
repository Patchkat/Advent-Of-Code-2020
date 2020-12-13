passport = []
necessary = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
total = 0
f = [x for x in open('passports.txt').readlines()]
for x in f:
    if not x in ['\n', '\r\n', ' ']:
        for y in x.rstrip('\n').split(' '):
            passport.append(y.split(":")[0])
    else:
        if passport.count('cid') == 1:
            passport.remove('cid')
        if len(passport) == 7:
            total += 1
        passport = []
print(total)