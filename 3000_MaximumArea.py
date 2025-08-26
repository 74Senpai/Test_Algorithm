import math

class Solution:
    # PASS: 4ms, 17.94MB
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        bigest_area = 0
        width_z = 0
        for i in dimensions:
            curr_width = math.sqrt(i[0] * i[0] + i[1] * i[1])
            if curr_width > width_z:
                width_z = curr_width
                bigest_area = i[0] * i[1]
            elif curr_width == width_z:
                bigest_area = max(bigest_area, i[0] * i[1])
        
        return bigest_area
            
