f = open('input.txt', 'r')
s = f.read().strip('\n')
f.close()

print(s)

# Part 1
ret = 0
for i in range(0, len(s)):
    if s[i] == s[i-1]:
        ret += int(s[i])
print(ret)

# Part 2
ret = 0
n = len(s)
for i in range(0, len(s)):
    if s[i] == s[int(i+n/2) % n]:
        ret += int(s[i])
print(ret)
