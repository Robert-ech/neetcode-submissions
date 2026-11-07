# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to reverse a linked list we have to create a prev pointer
        # we have to set nxt to next
        # then we have to swap where the poiter is facing so from curr to prev
        # then move the curr to prev
        # finally move nxt to curr
        prev = None
        curr = head # curr = head that was given

        while curr:
            nxt = curr.next # store the actual next curr
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


        