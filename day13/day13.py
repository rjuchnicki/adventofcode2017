d = {}
with open('input.txt', 'r') as f:
    for l in [x.split(': ') for x in f.readlines()]:
        d[int(l[0])] = int(l[1])

# s = '0: 3\n1: 2\n4: 4\n6: 4'
# d = {}
# for l in [x.split(': ') for x in s.split('\n')]:
#     d[int(l[0])] = int(l[1])

def severity(d, delay):
    severity = 0
    for i in d.keys():
        step = i + delay
        depth = d[i]
        if step % (2*depth - 2) == 0:
            severity += depth * step

    return severity

print('Part 1:', severity(d, 0))

delay = 0
while(True):
    if severity(d, delay) == 0:
        break
    delay += 1

print('Part 2:', delay)
