f = [x.rstrip('\n') for x in open('declarations.txt').readlines()]
total = 0
questions = []
beginning = -1
for pos, x in enumerate(f):
    if beginning == -1:
        beginning = pos
    if x not in ['\n', '']:
        for y in x:
            questions.append(y)
    else:
        answers = list(dict.fromkeys(questions))
        for y in answers:
            if questions.count(y) == pos - beginning:
                total += 1
        beginning = -1
        questions = []
total += len(list(dict.fromkeys(questions)))
print(total)