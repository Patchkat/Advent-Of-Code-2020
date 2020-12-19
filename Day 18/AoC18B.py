def solve_equation(equation):
    total = 0
    y = 0
    while y < len(equation):
        if equation[y] == '+':
            total = int(equation[y-1]) + int(equation[y+1])
            equation.pop(y-1)
            equation.pop(y-1)
            equation.pop(y-1)
            equation.insert(y-1, str(total))
        else:
            y += 1
    y = 0
    while y < len(equation):
        if equation[y] == '*':
            total = int(equation[y-1]) * int(equation[y+1])
            equation.pop(y-1)
            equation.pop(y-1)
            equation.pop(y-1)
            equation.insert(y-1, str(total))
        else:
            y += 1
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