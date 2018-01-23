with open('input.txt', 'r') as f:
    lines = [l.split(' <-> ') for l in f.readlines()]

pipes = {}
for l in lines:
    pipes[int(l[0])] = [int(x) for x in l[1].split(', ')]

def connect(s, pipes, programs):
    for p in programs:
        if p not in s:
            s.add(p)
            connect(s, pipes, pipes[p])

s = set()
connect(s, pipes, pipes[0])
print('Part 1:', len(s))

added = set()
groups = 0
for p in pipes:
    if p not in added:
        s = set()
        connect(s, pipes, pipes[p])
        groups += 1
        added = added.union(s)

print('Part 2:', groups)
