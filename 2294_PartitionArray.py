def partitionArray(self, nums: list[int], k: int) -> int:
    nums.sort()
    point_sub = nums[0]
    counter = 1
    for i in nums:
        if i - point_sub > k:
            point_sub = i
            counter += 1

    return counter                
