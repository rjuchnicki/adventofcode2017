import re

with open('input.txt', 'r') as f:
    inst = [x.strip('\n') for x in f.readlines()]

match = [re.match(r'(\w+) (inc|dec) (-*\d+) if (\w+) ([<>=!]+) (-*\d+)', i) for i in inst]

d = {}
for m in match:
    d[m.group(1)] = 0

execution_max = 0
for m in match:
    comp = m.group(5)
    x = d[m.group(4)]
    y = int(m.group(6))
    t = False
    if comp == '>' and x > y:
        t = True
    elif comp == '<' and x < y:
        t = True
    elif comp == '>=' and x >= y:
        t = True
    elif comp == '<=' and x <= y:
        t = True 
    elif comp == '==' and x == y:
        t = True
    elif comp == '!=' and x != y:
        t = True

    if t:
        if m.group(2) == 'inc':
            d[m.group(1)] += int(m.group(3))
        elif m.group(2) == 'dec':
            d[m.group(1)] -= int(m.group(3))

        if d[m.group(1)] > execution_max:
            execution_max = d[m.group(1)]

print('Part 1:', max(d.values()))
print('Part 2:', execution_max)
