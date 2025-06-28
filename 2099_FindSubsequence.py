def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == k:
            return nums
            
        nums = sorted(enumerate(nums), key=lambda i: i[1])
        nums = nums[len(nums) - k:]
        nums = sorted(nums, key=lambda i: i[0])
        nums = [val for i, val in nums]
        return nums