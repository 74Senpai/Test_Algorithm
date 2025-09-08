class Solution:
    #PASS : 0ms, 17,7MB
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n < 10:
            return [n - 1, 1]
        
        minus_var = int("1" * (len(str(n)) - 1))
        while minus_var < n:
            res = str(n - minus_var)
            if "0" not in res:
                return [minus_var, n - minus_var]
            minus_var += minus_var 
