f = open('input.txt', 'r')
reg = [int(x) for x in f.read().strip('\n').split()]

states = {}
s = ' '.join([str(x) for x in reg])
steps = 0
while s not in states:
    states[s] = steps
    max_i = reg.index(max(reg))
    n = reg[max_i]
    reg[max_i] = 0
    for i in range(n):
        reg[(max_i + i + 1) % len(reg)] += 1

    s = ' '.join([str(x) for x in reg])
    steps += 1

print('Part 1:', steps)
print('Part 2:', steps - states[s])
