# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2 pointers O(1) space O(n) time
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        ahead=behind=dummy
        for _ in range(n+1): # end exclusive as well
            ahead=ahead.next
        while ahead:
            behind=behind.next
            ahead=ahead.next
        behind.next=behind.next.next
        return dummy.next # not returning head as in case head is removed dummy.next still points to the right node whereas returning wouldn't 

        