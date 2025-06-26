class Ver1:
    # FAILD : Time Limit Error
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        len_nums = len(nums)
        if len_nums <= 3:
            if nums[0] + nums[1] + nums[2] != 0:
                return []
            return [nums]

        threeSum = []
        nums.sort()
        i_point, j_point, k_point = 0, 1, len_nums - 1
        while True:
            if i_point >= len_nums - 3 and j_point >= len_nums - 2 and k_point <= j_point + 1:
                break  
            i, j, k = nums[i_point], nums[j_point], nums[k_point]
            if i + j + k == 0:
                if [i,j,k] not in threeSum:
                    threeSum.append([i,j,k])
                j_point += 1
                k_point = len_nums - 1
            if k_point > j_point + 1:
                k_point -= 1
            else:
                if j_point < len_nums - 2:
                    j_point += 1
                else:
                    i_point += 1
                    j_point = i_point + 1
                k_point = len_nums - 1
                
        return threeSum
    
class Ver2:
    # PASS : Time >=  666ms < 700ms 
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        len_nums = len(nums)
        threeSum = []
        pass_3Sum = {}
        right = len_nums - 1
        for i in range(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            left = i + 1
            right = len_nums - 1
            while True:
                if left >= right:
                    break
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    key = (nums[i], nums[left], nums[right])
                    if key not in pass_3Sum:
                        threeSum.append(list(key))
                        pass_3Sum[key] = 1
                    left += 1
                    right -= 1  
                elif sum_ < 0:
                    left += 1  
                else:
                    right -= 1
                
        return threeSum

print(Ver2().threeSum([-1,0,1,2,-1,-4]))