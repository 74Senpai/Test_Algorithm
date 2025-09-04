class Solution:
    # PASS: 0ms, 17,52MB
    def findClosest(self, x: int, y: int, z: int) -> int:
        fist_person_to_G = abs(x - z)
        second_person_to_G = abs(y - z)
        
        if fist_person_to_G < second_person_to_G:
            return 1
        elif fist_person_to_G > second_person_to_G:
            return 2

        return 0
