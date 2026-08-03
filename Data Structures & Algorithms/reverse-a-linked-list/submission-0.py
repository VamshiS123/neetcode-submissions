# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # save temp as what current node points at
            temp = curr.next

            # update current.next to prev
            curr.next = prev

            # update prev to curr
            prev = curr

            # update curr to temp
            curr = temp
        
        return prev
            