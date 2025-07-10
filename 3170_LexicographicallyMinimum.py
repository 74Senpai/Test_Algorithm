import heapq
class Ver2:
    # TLE : 601/602 testcase passed
    def clearStars(self, s: str) -> str:
        ch_list = []
        heapq.heapify(ch_list)
        stack = []
        for ch in s:
            if ch != "*":
                heapq.heappush(ch_list, ch)
                stack.insert(0, ch)
            else:
                min_ch = heapq.heappop(ch_list)
                stack.remove(min_ch)
                        
        output = ''.join(stack[::-1])
        return output
    
    