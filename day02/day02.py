f = open('input.txt', 'r')
lines = [x.strip('\n') for x in f.readlines()]
f.close()


ret1 = 0  # Part 1
ret2 = 0  # Part 2
for l in lines:
    nums = [int(i) for i in l.split('\t')]
    ret1 += (max(nums) - min(nums))

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] % nums[j] == 0:
                ret2 += (nums[i] / nums[j])
                break

print(ret1)
print(ret2)
