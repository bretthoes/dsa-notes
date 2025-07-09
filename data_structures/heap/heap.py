class MinHeap:
    """
    Min-heap (priority queue) implemented with 0-based indexing.

    In a min-heap, the smallest element is at the root (index 0).
    For node at index i:
      - left child index: 2*i + 1
      - right child index: 2*i + 2
      - parent index: (i - 1) // 2 (for i > 0)

    Push and pop operations maintain the heap property in O(log n) time.
    """
    def __init__(self) -> None:
        """Initialize an empty min-heap."""
        self.heap = []

    def push(self, value: int) -> None:
        """
        Insert value into heap, maintaining min-heap property via sift-up.
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        i = len(self.heap) - 1
        # Sift up: while not at root and current < parent
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] >= self.heap[parent]:
                break
            # Swap child and parent
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def pop(self) -> int | None:
        """
        Remove and return the min element (root).
        Replace root with last element and sift-down to restore heap property.
        Time Complexity: O(log n)
        """
        # base cases
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # save return value, replace with last element in heap
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        # sift down
        i = 0
        n = len(self.heap)
        # while at least one child exists
        while (i * 2) + 1 < n:
            left = (i * 2) + 1
            right = (i * 2) + 2
            smallest = i
            # get the smallest between left, right and i
            if left < n and self.heap[left] < self.heap[i]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            # if i is the smallest (we didnt update), we can break
            # since the children are both larger
            if smallest == i:
                break

            # otherwise, swap and update i
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        # return the value we saved before loop
        return root_value
        
    def heapify(self, data: list[int]) -> None:
        """
        Build the heap from the given list via bottom-up approach
        After calling this, self.heap should be a valid min-heap containing all elements from data.
        Time Complexity: O(n)
        """
        #copy original list
        self.heap = data[:]

        #base case
        n = len(self.heap)
        if n <= 1:
            return

        # dont need to start with leaf nodes since they have no children
        # to compare against; get index of first parent node and iterate backwards
        last_parent = (n - 2) // 2
        for i in range(last_parent, -1, -1):
            # begin sifting parent node downwards as needed
            cur = i
            while True:
                left = (cur * 2) + 1
                right = (cur * 2) + 2
                smallest = cur

                if left < n and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < n and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if smallest == cur:
                    break

                self.heap[cur], self.heap[smallest] = self.heap[smallest], self.heap[cur]
                cur = smallest







