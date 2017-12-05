f = open('input.txt', 'r')
lines = [int(x.strip('\n')) for x in f.readlines()]
f.close()

# Part 1
i = 0
steps = 0
while i < len(lines):
    tmp = lines[i]
    lines[i] += 1
    i += tmp
    steps+=1
    
print('Part 1:', steps)

# Part 2
i = 0
steps = 0
while i < len(lines):
    tmp = lines[i]
    if tmp >= 3:
        lines[i] -= 1
    else:
        lines[i] += 1
    i += tmp
    steps+=1

print('Part 2:', steps)
