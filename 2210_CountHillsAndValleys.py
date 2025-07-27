class Ver1:
    # 0ms, 18MB
    def countHillValley(self, nums: list[int]) -> int:
        counter = 0
        other_hill = -1
        for i in range(1, len(nums) - 1):
            if i < other_hill:
                continue
            curr = nums[i]
            left, right = nums[i - 1], nums[i + 1]
            other_hill = i + 1
            if curr == left :
                move = i - 2
                while curr == left and move >= 0:
                    left = nums[move]
                    move -= 1  
            if curr == right:
                move = i + 2
                while curr == right and move < len(nums):
                    right = nums[move]
                    move += 1   
                other_hill = min(len(nums), move - 1)

            if (curr > left and curr > right) or (curr < left and curr < right):
                counter += 1

        return counter