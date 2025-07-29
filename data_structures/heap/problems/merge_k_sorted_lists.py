from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        ideas:
        need to do somethin similar to mergesort algorithm. need to track each head
        of the k lists, maybe in a minheap, and pop off onto a new linked list that
        will contain all values. If we pop off a value, we need to update that pointer
        to its next value
        """
        dummy = ListNode()
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        cur = dummy
        while heap:
            val, i, head = heapq.heappop(heap)
            if head.next:
                heapq.heappush(heap, (head.next.val, i, head.next))
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next

        
