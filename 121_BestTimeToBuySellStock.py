class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 10**4
        max_ = 0
        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > max_:
                max_ = i - buy
        return max_ 