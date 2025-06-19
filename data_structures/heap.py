
class MaxHeap:
    """
    Max-heap (priority queue) implemented with 0-based indexing.

    In a max-heap, the largest element is at the root (index 0).
    For node at index i:
      - left child index: 2*i + 1
      - right child index: 2*i + 2
      - parent index: (i - 1) // 2 (for i > 0)

    Push and pop operations maintain the heap property in O(log n) time.
    """
    def __init__(self) -> None:
        """Initialize an empty max-heap."""
        self.heap = []

    def __len__(self) -> int:
        """Return number of elements in heap."""
        return len(self.heap)

    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return not self.heap

    def push(self, value: int) -> None:
        """
        Insert value into heap, maintaining max-heap property via sift-up.
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        i = len(self.heap) - 1
        # Sift up: while not at root and current > parent
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] <= self.heap[parent]:
                break
            # Swap child and parent
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def peek(self) -> int | None:
        """Return the max element without removing it, or None if empty."""
        if self.heap:
            return self.heap[0]
        return None

    def pop(self) -> int | None:
        """
        Remove and return the max element (root).
        Replace root with last element and sift-down to restore heap property.
        Time Complexity: O(log n)
        """
        if not self.heap:
            return None
        n = len(self.heap)
        if n == 1:
            return self.heap.pop()
        # Save root value to return
        root_value = self.heap[0]
        # Move last element to root
        self.heap[0] = self.heap.pop()
        # Sift down from root
        i = 0
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            # Check left child
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            # Check right child
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i:
                break
            # Swap current with larger child
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
        return root_value


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

    def __len__(self) -> int:
        """Return number of elements in heap."""
        return len(self.heap)

    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return not self.heap

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

    def peek(self) -> int | None:
        """Return the min element without removing it, or None if empty."""
        if self.heap:
            return self.heap[0]
        return None

    def pop(self) -> int | None:
        """
        Remove and return the min element (root).
        Replace root with last element and sift-down to restore heap property.
        Time Complexity: O(log n)
        """
        if not self.heap:
            return None
        n = len(self.heap)
        if n == 1:
            return self.heap.pop()
        # Save root value to return
        root_value = self.heap[0]
        # Move last element to root
        self.heap[0] = self.heap.pop()
        # Sift down from root
        i = 0
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            # Check left child
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Check right child
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            # Swap current with smaller child
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
        return root_value


if __name__ == "__main__":
    # Example usage for MaxHeap
    max_h = MaxHeap()
    for v in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
        max_h.push(v)
    print("MaxHeap pop sequence:", [max_h.pop() for _ in range(len(max_h))])

    # Example usage for MinHeap
    min_h = MinHeap()
    for v in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
        min_h.push(v)
    print("MinHeap pop sequence:", [min_h.pop() for _ in range(len(min_h))])
