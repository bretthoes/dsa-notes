class node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node to the end of the list. 
        Time Complexity: O(n)"""
        if not self.head:
            self.head = node(value)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = node(value)

    def prepend(self, value):
        """Add a node to the beginning of the list. 
        Time Complexity: O(1)"""
        self.head = node(value, self.head)

    def insert(self, index, value):
        """Insert a node at a specific index. 
        Time Complexity: O(n)"""
        counter = 0
        cur = self.head
        prev = None
        while cur:
            if index == counter:
                if prev:
                    prev.next = node(value, cur)
                else:
                    self.head = node(value, self.head)
                return
            prev = cur
            cur = cur.next
            counter += 1

        if index == counter:
            if prev:
                prev.next = node(value)
            else:
                self.head = node(value)
            return

        raise IndexError('Index not valid')

    def delete(self, value):
        """Delete the first node with the given value. 
        Time Complexity: O(n)"""
        cur = self.head
        prev = None

        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev = cur
            cur = cur.next

    def delete_at_index(self, index):
        """Delete the node at a specific index. 
        Time Complexity: O(n)"""
        counter, cur, prev = 0, self.head, None

        while cur:
            if counter == index:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev = cur
            counter += 1
            cur = cur.next

    def search(self, value):
        """Return the index of the first occurrence of value. 
        Time Complexity: O(n)"""
        counter, cur = 0, self.head
        while cur:
            if cur.value == value:
                return counter
            counter += 1
            cur = cur.next
        return -1

    def is_empty(self):
        """Check if the list is empty. 
        Time Complexity: O(1)"""
        return not self.head

    def length(self):
        """Return the number of elements in the list. 
        Time Complexity: O(n)"""
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        return count

    def reverse(self):
        """Reverse the linked list in-place. 
        Time Complexity: O(n)"""
        cur = self.head
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        self.head = prev

    def to_list(self):
        """Convert the linked list to a Python list. 
        Time Complexity: O(n)"""
        arr, cur = [], self.head
        while cur:
            arr.append(cur.value)
            cur = cur.next
        return arr

