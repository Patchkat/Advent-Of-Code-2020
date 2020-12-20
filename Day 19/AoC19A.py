def validate(input_string, num):
    # Author: https://github.com/val-is
    if input_string == "":
        return False
    
    rule = rules.get(num)

    if rule in ["a", "b"]:
        return rule == input_string
    
    for ru in rule:
        if len(ru) == 1:
            if memoize(input_string, int(ru[0])):
                return True
        if len(ru) == 2:
            for split in range(1, len(input_string)):
                a, b = input_string[:split], input_string[split:]
                if memoize(a, int(ru[0])) and memoize(b, int(ru[1])):
                        return True
        if len(ru) == 3:
            for x in range(1, len(input_string)):
                for y in range(x, len(input_string)):
                    a, b, c = input_string[:x], input_string[x:y], input_string[y:]
                    if not (a == '' or b == '' or c == ''):
                        if (memoize(a, int(ru[0])) and memoize(b, int(ru[1]))
                            and memoize(c, int(ru[2]))):
                                return True

    return False

def memoize(inp_str, num):
    tests = (inp_str, num)
    if tests in memoized:
        return memoized[tests]
    result = validate(inp_str, num)
    memoized[tests] = result
    return result

f = [x.rstrip('\n') for x in open('input.txt').readlines()]
x = 0
rules = {}
memoized = {}
while f[x] != '':
    num, rule = f[x].split(': ') 
    if '|' in rule:
        parts = rule.split(" | ")
        rules[int(num)] = [parts[0].split(' '), parts[1].split(' ')]
    elif rule in ['\"a\"', '\"b\"']:
        rules[int(num)] = rule[1]
    else:
        rules[int(num)] = [rule.split(' ')]
    x += 1

x += 1
total = 0
while x < len(f):
    test_input_string = f[x]
    if validate(test_input_string, 0):
        total += 1
    x += 1
print(total)