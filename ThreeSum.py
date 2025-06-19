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
