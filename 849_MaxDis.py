def maxDistToClosest(self, seats: list[int]) -> int:
    len_seats = len(seats)
    x, y = -1,-1
    max_dis = 1
    for i in range(len_seats):
        if seats[i] == 1:
            if x == -1:
                x = i
                max_dis = i
            elif y == -1 or y == x:
                y = i
                max_dis = max(max_dis, ((y - x) // 2))
                x = y

    max_dis = max(max_dis, len_seats - 1 - x)
    return max_dis

print(maxDistToClosest(None, [1,0,0,0,1,0,1]))