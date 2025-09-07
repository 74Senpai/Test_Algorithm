class Solution:
    # PASS: 0ms, 17,76MB
    def sumZero(self, n: int) -> List[int]:
        arr = []
        for i in range(n, 1, -2):
            arr.append(i)
            arr.append(-i)

        if n % 2 == 1:
            arr.append(0)
        return arr

