def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
    new_list = []
    nums.sort()
    stop = len(nums)
    for i in range(0, stop, 3):
        if nums[i+2] - nums[i] > k:
            return []
        new_list.append([nums[i], nums[i+1], nums[i+2]])

    return new_list