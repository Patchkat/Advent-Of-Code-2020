# Function used to evaluate equations using the new order of operations
def solve_equation(equation):
    total = 0
    loop = 0
    while loop < len(equation):
        if equation[loop] == '+':
            total = int(equation[loop-1]) + int(equation[loop+1])
            equation.pop(loop-1)
            equation.pop(loop-1)
            equation.pop(loop-1)
            equation.insert(loop-1, str(total))
        else:
            loop += 1
    loop = 0
    while loop < len(equation):
        if equation[loop] == '*':
            total = int(equation[loop-1]) * int(equation[loop+1])
            equation.pop(loop-1)
            equation.pop(loop-1)
            equation.pop(loop-1)
            equation.insert(loop-1, str(total))
        else:
            loop += 1
    return total


f = [equations.rstrip('\n') for equations in open('input.txt').readlines()]
total = 0
for loop, _ in enumerate(f):
    equation_final = f[loop].replace(' ', '')
    equation_final = [c for c in x]
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