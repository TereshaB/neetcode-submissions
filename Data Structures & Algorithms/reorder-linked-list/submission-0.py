# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next # mid of the list
        # if odd one more element is considered in the first half
        slow.next=None # splitting the list in 2 halves
        prev=None
        while second: # reverse second half
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        # merge the 2 halves 
        first=head
        second=prev
        while second: # second could be lesser in size than first but never greater 
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2

