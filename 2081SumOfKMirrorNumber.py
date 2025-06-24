class Solution:
    def kMirror(self, k: int, n: int) -> int:
        i = 1
        total_num = 1
        while n > 1:
            i += 1
            if str(i) != str(i)[::-1]:
                continue
                
            number = i
            digits = ""
            if k != 2:
                while number:
                    digits += str(number % k)
                    number //= k
            else:
                digits = str(bin(number)[2:])

            if int(digits) == int(digits[::-1]):
                total_num += i
                print(i)
                n -= 1
            
        return total_num