# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointers = {}
        while head:
            if head.next in pointers:
                return True
            else:
                pointers[head.next] = 0
            head = head.next
        return False

