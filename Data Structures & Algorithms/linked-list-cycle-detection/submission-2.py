# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = head
        fast = fast.next
        if fast:
            fast = fast.next
        else:
            return False
        slow = head

        while fast:
            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next
            else:
                return False
        
        return False
            

            


