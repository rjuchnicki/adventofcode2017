f = open('input.txt', 'r')
lines = [x.strip('\n') for x in f.readlines()]
f.close()

# Part 1
ret = 0
for l in lines:
    nums = [int(i) for i in l.split('\t')]
    ret += (max(nums) - min(nums))
print(ret)

# Part 2
ret = 0
for l in lines:
    nums = [int(i) for i in l.split('\t')]
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] % nums[j] == 0:
                ret += (nums[i] / nums[j])
            elif nums[j] % nums[i] == 0:
                ret += (nums[j] / nums[i])
print(ret)
