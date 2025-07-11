class Ver1:
    # 100 % TLE, O(n**3)
    # Need use two point left and right + sort
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for z in range(j + 1, len(nums)):
                    cur = nums[i] + nums[j] + nums[z]
                    if abs(target - cur) < abs(target - closest):
                        closest = cur

        return closest

print(Ver1().threeSumClosest([-1,2,1,-4], 1))

class Ver2:
    #PASS : 390ms, 18MB
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = nums[left] + nums[right] + nums[i]
                if cur < target:
                    left += 1
                else:
                    right -= 1

                if abs(cur - target) < abs(closest - target):
                    closest = cur

        return closest