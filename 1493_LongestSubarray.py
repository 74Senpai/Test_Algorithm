class Solution:
    #PASS: 20ms, 21,72MB
    def longestSubarray(self, nums: List[int]) -> int:
        i, _max, count, minus = 0, 0, 0, -1
        len_n = len(nums)
        
        while i < len_n:
            if nums[i] == 1:
                count += 1
            elif count > 0:
                if minus == -1:
                    minus = i
                else:
                    _max = max(_max, count)
                    count = 0
                    i = minus
                    minus = -1
            i += 1

        _max = max(_max, count)
        if _max == len_n:
            return _max - 1

        return _max
