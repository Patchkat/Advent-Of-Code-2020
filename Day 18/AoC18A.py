def solve_equation(equation):
    total = 0
    for y in range(len(equation)):
        if equation[y] == '+':
            total = int(equation[y-1]) + int(equation[y+1])
            equation[y+1] = str(total)
        elif equation[y] == '*':
            total = int(equation[y-1]) * int(equation[y+1])
            equation[y+1] = str(total)
    return total


f = [x.rstrip('\n') for x in open('input.txt').readlines()]
total = 0
for y, _ in enumerate(f):
    x = f[y].replace(' ', '')
    x = [c for c in x]
    order = []
    while len(x) > 0:   
        order.append(x.pop(0))
        if order[-1] == ')':
            item = order.pop()
            equation = []
            while item != '(':
                equation.insert(0, item)
                item = order.pop()
            order.append(str(solve_equation(equation)))
    if len(order) > 0:
        total += solve_equation(order)
print(total)       