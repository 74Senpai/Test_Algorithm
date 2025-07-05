class Ver1:
    #3ms, 18MB
    def findLucky(self, arr: list[int]) -> int:
        nums_map = {}
        for num in arr:
            nums_map[num] = nums_map.get(num, 0) + 1

        lucky_num = -1
        for key in nums_map:
            if nums_map[key] == key:
                lucky_num = max(lucky_num, key)
        return lucky_num
    
class Ver2:
    #3ms, 18MB
    def findLucky(self, arr: list[int]) -> int:
        nums_map = {}
        arr.sort()
        for i in range(len(arr) - 1, -1, -1):
            nums_map[arr[i]] = nums_map.get(arr[i], 0) + 1
            if nums_map[arr[i]] == arr[i] and (arr[i - 1] != arr[i] or i == 0 ):
                return arr[i]
                
        return -1 
    
class Ver3: 
    # 0ms ~ 2ms, 17.65 MB
    def findLucky(self, arr: list[int]) -> int:
        arr.sort()
        i = len(arr)
        if arr[0] == arr[-1] and arr[0] == i:
            return arr[0]
            
        pass_ = -1
        while i >= 0:
            i -= 1
            curr = arr[i]
            len_i = i - curr + 1
            if len_i < 0:
                continue
            if arr[len_i] == curr and curr != pass_:
                if arr[len_i - 1] != curr:
                    return curr

                pass_ = curr
                i = len_i - 1

        return -1    
    
print(Ver3().findLucky([2,2,3,4]))