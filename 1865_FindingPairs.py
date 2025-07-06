class Ver1:
    # TLE 18 / 26 testcases passed
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2     

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        counter = 0
        for i in self.nums1:
            for j in self.nums2:
                if i + j == tot:
                    counter += 1

        return counter
    
class Ver2:
    # TLE : 25 / 26 testcases passed
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2     

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        counter = 0
        needed_num = {}
        for i in self.nums1:
            needed_num[tot - i] = needed_num.get(tot - i, 0) + 1

        for j in self.nums2:
            if j in needed_num:
                counter += needed_num[j]

        return counter
    
class Ver3:
    # TLE : 24 / 26 
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.map_nums1 = {}     

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        counter = 0
        if self.map_nums1 == {}:
            for i in self.nums1:
                self.map_nums1[i] = self.map_nums1.get(i, 0) + 1

        for j in self.nums2:
            counter += self.map_nums1.get(tot - j, 0)

        return counter

from collections import Counter    
class Ver4:
    # PASS : 230 ms, 50 MB 
    # Can change Counter to dict
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.map_nums1 = {}
        for i in self.nums1:
            self.map_nums1[i] = self.map_nums1.get(i, 0) + 1  

        self.counter2 = Counter(nums2)  
    
        # self.counter2 = {}
        # for i in self.nums2:
        #     self.counter2[i] = self.counter2.get(i, 0) + 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        if self.counter2[old_val] > 1 :
            self.counter2[old_val] -= 1
        else:
            del self.counter2[old_val]
        
        self.nums2[index] += val
        self.counter2[old_val + val] += 1
        
        # self.counter2[old_val + val] = self.counter2.get(old_val + val, 0) + 1

    def count(self, tot: int) -> int:
        counter = 0
        for key in self.map_nums1:
            counter += self.map_nums1[key] * self.counter2.get(tot - key, 0)

        return counter 