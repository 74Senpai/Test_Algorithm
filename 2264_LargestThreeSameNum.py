class Solution:
    # PASS: 0ms, 17.98MB
    def largestGoodInteger(self, num: str) -> str:
        max_num = ""
        for i in range(1, len(num) - 1):
            if num[i] == num[i - 1] == num[i + 1] and (max_num == "" or max_num[0] < num[i] ):
                max_num = num[i]
                if max_num == "9":
                    break
        return max_num * 3