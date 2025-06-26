class V1:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0,0
        move = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
        max_dis = 0
        for ch in s:
            move_x, move_y = move[ch]
            dis = abs(x + move_x) + abs(y + move_y)
            if k > 0:
                dir_change = ch
                for dir_ in "NSEW":
                    if dir_ != ch:
                        dis_x, dis_y = move[dir_]
                        curr_dis = abs(x + dis_x) + abs(y + dis_y)
                        if curr_dis > dis:
                            dis = curr_dis
                            dir_change = dir_
                if dir_change != ch : 
                    print("Change: ",ch," to:", dir_change)
                    move_x, move_y = move[dir_change]
                    k -= 1
            max_dis = max(max_dis, dis)
            x += move_x
            y += move_y

        return max_dis
    
print(V1().maxDistance("WEES", 2))