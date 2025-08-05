class Ver1:
    #PASS: 21ms, 17.74MB
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        isUse = set()
        for i in fruits:
            for j in range(len(baskets)):
                if j in isUse:
                    continue
                if baskets[j] >= i:
                    isUse.add(j)
                    break

        return len(fruits) - len(isUse)
    
class Ver2:
    #PASS: 13ms, 17.90MB
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        for i in fruits:
            for j in range(len(baskets)):
                if baskets[j] >= i:
                    baskets.pop(j)
                    break

        return len(baskets)