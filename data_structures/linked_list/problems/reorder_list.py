from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use slow and fast ptrs to reverse 2nd half of linked list
        # keep a reference of 2nd half start
        # build list by alternating between pointing to both halves
        # O(n)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse mid -> end
        curr, prev = slow, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first, second = head, prev
        while first and second:
            tmp_first, tmp_second = first.next, second.next
            first.next, second.next = second, tmp_first
            first, second = tmp_first, tmp_second





        
