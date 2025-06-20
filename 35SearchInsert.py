class V1:
    def searchInsert(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        if nums[-1] < target:
            return len_nums
        if nums[0] > target:
            return 0
        for i in range(len_nums):
            if nums[i] >= target:
                return i

        return len_nums
    
class V2:
    def searchInsert(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        if nums[-1] < target:
            return len_nums
        if nums[0] >= target:
            return 0
        left, right = 0 , len_nums - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

                
print(V2().searchInsert([1, 3, 5, 6], 2))