class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_map = {}
        for num in str(n):
            n_map[num] = n_map.get(num, 0) + 1

        len_n = len(str(n))

        for i in range(32):
            curr = 2 ** i
            curr_str = str(curr)
            if len(curr_str) > len_n:
                return False
            
            if len(curr_str) != len_n:
                continue

            temp_map = n_map.copy()
            flag = True
            for digit in curr_str:
                if digit not in temp_map or temp_map[digit] == 0:
                    flag = False
                    break
                temp_map[digit] -= 1
            
            if flag:
                return True

        return False
