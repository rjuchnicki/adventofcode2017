with open('input.txt', 'r') as f:
    inp = f.read().strip('\n')

def compute_score(inp):
    garbage = False
    garb_n = 0
    score = 0
    nest = 0
    i = 0
    while i < len(inp):
        if garbage:
            if inp[i] == '>':
                garbage = False
            elif inp[i] == '!':
                i += 2
                continue
            else:
                garb_n += 1
        else:
            if inp[i] == '{':
                nest += 1
            elif inp[i] == '}':
                score += nest
                nest -= 1
            elif inp[i] == '<':
                garbage = True

        i += 1
    return score, garb_n

assert(compute_score('{}')[0] == 1)
assert(compute_score('{{{}}}')[0] == 6)
assert(compute_score('{{}, {}}')[0] == 5)
assert(compute_score('{{{},{},{{}}}}')[0] == 16)
assert(compute_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9)
assert(compute_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9)

score, garb_n = compute_score(inp)
print('Part 1:', score)
print('Part 2:', garb_n)
