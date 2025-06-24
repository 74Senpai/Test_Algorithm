class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        set_nums = set(nums)
        if len(set_nums) == 1:
            x = []
            x += range(0,len(nums), 1)
            return x
            
        set_output = set()
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] == key:
                for x in range(max(i - k, 0), min(i + k + 1, len_nums), 1):
                    set_output.add(x)
                    if x == len_nums:
                        break

        return list(set_output)