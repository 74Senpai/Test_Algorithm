def numSubseq(self, nums: list[int], target: int) -> int:
    nums.sort()
    MOD = 10**9 + 7
    result = 0
    len_nums = len(nums)
    x = len_nums - 1
    for i in range(len_nums):
        if x < i:
            break
        while x >= i:
            if nums[x] + nums[i] <= target:
                result = (result + (2**(x - i))) % MOD
                break
            x -= 1
            
    return result 

print(numSubseq(None, [2,3,3,4,6,7], 12))