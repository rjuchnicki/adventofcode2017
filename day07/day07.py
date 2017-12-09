with open('input.txt', 'r') as f:
    lines = [x.strip('\n') for x in f.readlines()]

# Part 1
d = {}
new_lines = []
for l in lines:
    parts = l.split('-> ')
    support = parts[0].split(' ')[0]
    supported = []
    if len(parts) > 1:
        supported = parts[1].split(', ')
        for s in supported:
            d[s] = 1
    new_lines.append(support)

for n in new_lines:
    if n not in d:
        print('Part 1:', n)
