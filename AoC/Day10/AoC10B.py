def get_paths(attachments):
    paths = {x : 0 for x in attachments.keys()}
    x = len(f) - 1
    paths[f[x]] = 1
    while x >= 0:
        for y in attachments.get(f[x]):
            paths[f[x]] += paths[y]
        x -= 1
    return paths


f = [int(x.rstrip('\n')) for x in open('adapters.txt').readlines()]
f.insert(0, 0)
f.sort()
f.append(max(f) + 3)
attachments = {}
for x in range(len(f)):
    attachment = []
    for y in range(1, 4):
        if x+y < len(f):
            if f[x+y] - f[x] < 4:
                attachment.append(f[x+y])
    attachments[f[x]] = attachment
print(get_paths(attachments)[0])