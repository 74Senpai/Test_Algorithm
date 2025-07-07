
class Ver1:
    # FAILD : 38/45 test case passed
    def maxEvents(self, events: list[list[int]]) -> int:
        events = sorted(events, key=lambda x: x[1])
        join = 0
        can_join = 1
        for event in events:
            if event[0] >= can_join: 
                join += 1
                can_join += 1
            elif event[1] >= can_join:
                join += 1
                can_join += 1
        
        return join

print(Ver1().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))