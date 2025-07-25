class Ver1:
    #3ms, 17.74MB
    def maxSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        seen = set()
        max_sum = nums[0]
        seen.add(nums[0])
        for i in nums:
            if i in seen:
                continue
            max_sum = max(max_sum, max_sum + i, i)
            seen.add(i)

        return max_sum
    
class Ver2:
    #0ms, 17.71MB
    def maxSum(self, nums: list[int]) -> int:
        max_sum = max(nums)
        if max_sum < 0:
            return max_sum
        max_sum = 0
        seen = set()
        for i in nums:
            if i >= 0 and i not in seen:
                max_sum += i
                seen.add(i)

        return max_sum