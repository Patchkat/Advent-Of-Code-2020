f = [x.rstrip('\n') for x in open('declarations.txt').readlines()]
total = 0
questions = []
for x in f:
    if x not in ['\n', '']:
        for y in x:
            questions.append(y)
    else:
        total += len(list(dict.fromkeys(questions)))
        questions = []
total += len(list(dict.fromkeys(questions)))
print(total)