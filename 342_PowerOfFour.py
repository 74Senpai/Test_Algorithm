class Ver1:
    #3ms, 17.62MB
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: 
            return True
            
        i = 1 
        curr = 4 ** 1
        while curr < n :
            i += 1
            curr = 4 ** i

        return curr == n
    
