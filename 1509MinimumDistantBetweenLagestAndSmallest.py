def minDifference(self, nums: list[int]) -> int:
    len_nums = len(nums)
    if len_nums <= 4: 
        return 0

    nums.sort()
    return min(
        nums[-1] - nums[3],
        nums[-2] - nums[2],
        nums[-3] - nums[1],
        nums[-4] - nums[0]
    )

print(minDifference(None, [6,6,0,1,1,4,6]))