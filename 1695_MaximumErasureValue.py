class Ver1:
    # FAILD: Logic wrong 
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        l = r = 0
        score = 0
        output = 0
        counter = dict()
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in counter:
                score += curr
                counter[curr] = score
            else:
                output = max(output, score)
                score -= counter[curr]
                counter[curr] = score + curr
                score = counter[curr]
            
        return max(output, score)
    
class Ver2:
    #PASS : use sliding window tech
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)

        return max_sum