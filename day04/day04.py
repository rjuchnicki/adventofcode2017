f = open('input.txt', 'r')
passphrases = [x.strip('\n') for x in f.readlines()]
f.close()

# Part 1
invalid = 0
for p in passphrases:
    d = {}
    for word in p.split():
        if word not in d:
            d[word] = 1
        else:
            invalid += 1
            break
print('Part 1:', len(passphrases) - invalid)

# Part 2
invalid = 0
for p in passphrases:
    d = {}
    for word in p.split():
        s = ''.join(sorted(word))
        if s not in d:
            d[s] = 1
        else:
            invalid += 1
            break
print('Part 2:', len(passphrases) - invalid)

