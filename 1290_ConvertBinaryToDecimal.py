# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #PASS : 0ms, 17.58 MB
    def getDecimalValue(self, head: ListNode) -> int:
        binary_num = ""
        while head != None:
            binary_num += str(head.val)
            head = head.next

        return int(binary_num, 2)