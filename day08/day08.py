import re

with open('input.txt', 'r') as f:
    inst = [x.strip('\n') for x in f.readlines()]

match = [re.match(r'(\w+) (inc|dec) (-*\d+) if (\w+) ([<>=!]+) (-*\d+)', i) for i in inst]

d = {}
for m in match:
    d[m.group(1)] = 0

exec_max = 0
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

        if d[m.group(1)] > exec_max:
            exec_max = d[m.group(1)]

print('Part 1:', max(d.values()))
print('Part 2:', exec_max)


# Cleaned up the solution after looking up how to access the comparison
# operators.
import operator as op
from collections import defaultdict

comps = {'>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '==': op.eq,
         '!=': op.ne}
ops = {'inc': 1, 'dec': -1}

exec_max = 0
d = defaultdict(int)
for reg, op, inc, _, x, c, y in [i.split() for i in inst]:
    if comps[c](d[x], int(y)):
        d[reg] += int(inc) * ops[op]
    exec_max = max(exec_max, d[reg])

print('Part 1:', max(d.values()))
print('Part 2:', exec_max)
