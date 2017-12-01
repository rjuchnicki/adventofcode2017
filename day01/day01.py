f = open('input.txt', 'r')
s = f.read()
f.close()

# Part 1
ret = 0
c = s[0]
for i in range(1, len(s)):
    if s[i] == c:
        ret += int(c)
    else:
        c = s[i]

if s[-2] == s[0]:
    ret += int(s[-2])
print(ret)

# Part 2
ret = 0
n = len(s)
for i in range(0, len(s)):
    if s[i] == s[int(i+n/2) % (n-1)]:
        ret += int(s[i])
print(ret)
