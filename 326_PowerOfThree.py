class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(32):
            curr = 3 ** i
            if curr == n: 
                return True
            if curr > n:
                return False
        return False
