class Solution:
    #PASS : 0ms, 17.74MB
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        less = len(v1) - len(v2)
        if less < 0:
            v1 += [0] * abs(less)
        elif less > 0:
            v2 += [0] * less
        
        for i1, i2 in zip(v1, v2):
            if int(i1) < int(i2):
                return -1
            if int(i1) > int(i2):
                return 1      

        return 0
        
