def divideString(self, s: str, k: int, fill: str) -> List[str]:
        need_fill = k - len(s) % k
        if need_fill != k and need_fill != 0:
            s = s + (fill * need_fill)
        divide_s = []
        for i in range(0, len(s) - (k - 1), k):
            divide_s.append(s[i:i+k])
        return divide_s