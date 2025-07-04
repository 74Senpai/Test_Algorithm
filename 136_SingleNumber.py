class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = nums[0]
        for i in nums[1:]:
            xor = xor ^ i
        return xor