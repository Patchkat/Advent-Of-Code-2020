def sum_nums(nums):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if x != y:
                if int(nums[x]) + int(nums[y]) == 2020:
                    return int(nums[x]) * int(nums[y])
nums = []
for x in open("./expenses.txt").readlines():
    nums.append(x.rstrip())
print(sum_nums(nums))
