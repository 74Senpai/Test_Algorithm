class Ver1:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            curr = 2 ** i
            if curr > n: 
                break
            if curr == n:
                return True
        return False 
            
