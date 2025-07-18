class Ver1:
    def maximumLength(self, nums: list[int]) -> int:
        even_count = 0
        dp_oddEven = []
        dp_evenOdd = []
        for i in nums:
            isEven = i % 2
            if isEven == 0:
                even_count += 1
            
            if dp_oddEven != []:
                if dp_oddEven[-1] != isEven:
                    dp_oddEven.append(isEven)
            elif isEven == 1:
                dp_oddEven.append(isEven)
            
            if dp_evenOdd != []:
                if dp_evenOdd[-1] != isEven:
                    dp_evenOdd.append(isEven)
            elif isEven == 0:
                dp_evenOdd.append(isEven)
        
        return max(even_count, len(nums) - even_count, len(dp_evenOdd), len(dp_oddEven))
    

class Ver2:
    def maximumLength(self, nums: list[int]) -> int:
        # Event == 0 , Odd == 1, c == case
        if len(nums) == 2 :
            return 2
        
        c00 = c01 = c11 = c10 = 0
        for i in nums:
            if i % 2 == 0:
                c00 += 1
                c10 = c01 + 1
            else:
                c11 += 1
                c01 = c10 + 1
        
        return max(c00, c10, c11, c01)
