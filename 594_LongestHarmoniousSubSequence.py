class Ver1:
    # Two point : TLE
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        longest_sub = 0
        for i in range(len(nums)):
            x = len(nums) - 1
            while i < x :
                if nums[x] - nums[i] == 1:
                    longest_sub = max(longest_sub, x - i + 1)
                    break
                x -= 1
                
        return longest_sub
    

class Ver2:
    # Two point but do not start right point at len
    # PASS: 58ms /18.88 MB 
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        longest_sub = 0
        left, right = 0, 1
        while left <= right and right < len_nums:
            minus = nums[right] - nums[left]
            if minus == 1:
                longest_sub = max(longest_sub, right - left + 1)
                right += 1
            else:
                if minus == 0 :
                    right += 1
                else:
                    left += 1

        return longest_sub
    
class Ver3:
    # hash table
    def findLHS(self, nums: list[int]) -> int:
        map_num = {}
        for i in nums:
            map_num[i] = map_num.get(i, 0) + 1

        longest_sub = 0
        sorted_keys = sorted(map_num)
        for key_a, key_b in zip(sorted_keys[:-1], sorted_keys[1:]):
            if key_b - key_a == 1:
                longest_sub = max(longest_sub, map_num[key_a] + map_num[key_b]) 

        return longest_sub
    
print(Ver3().findLHS([1,3,2,2,5,2,3,7]))