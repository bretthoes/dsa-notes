"""
Fast and Slow pointer algorithm
a.k.a. Floyd's Tortoise and Hare
"""

# Find the middle of a linked list
# Time: O(n), Space: O(1)
def findMiddle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# Determine if a linked list has a cycle
def hasCycle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

# Return the head of a cycle in a linked list
def getCycleStart(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if slow != fast:
        return None

    slow2 = head
    while slow == slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow



