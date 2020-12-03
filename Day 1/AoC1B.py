def sum_nums(nums):
    for x in range(len(nums)):
        for y in range(len(nums)):
            for z in range(len(nums)):
                if x != y and y != z and x != z:
                    if int(nums[x]) + int(nums[y]) + int(nums[z]) == 2020:
                        return int(nums[x]) * int(nums[y]) * int(nums[z])
nums = []
for x in open("./expenses.txt").readlines():
    nums.append(x.rstrip())
print(sum_nums(nums))
