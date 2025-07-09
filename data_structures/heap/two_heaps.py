"""
In some scenarios, we may require two heaps for an optimal algorithm.

Example:
Imagine a Median finder, where you simply need to find the median of a list.
But, you aren't provided the list up front, but rather as a stream of values.
The values are not in sorted order, and you still need to be able to return
the median when requested, but also account for new unsorted values to the
structure that may be added later.

We need to:
1. Insert new values into sorted order
2. Return the median of the current list of values when requested

Naively, we could solve this by appending every new value to an array.
We get the median by using half the length of the array,and returning
the value at that index (or the average of the two values if the list
is even in length). 
When we get a new value, we could iterate through our array and store
it in the correct ordered position.
This approach gives us constant time O(1) for finding the median, and
linear time O(n) for insertion.

With two heaps however, we could do the insert in O(log n), which greatly
improves performance as the list size increases (getting median would
still be constant time).

With the two heaps approach, we will name one of the heaps "small" which
will be a maxheap, and the other "large" which will be a minheap.
(Recall that a maxheap pops the largest value off first, and a minheap
pops the smallest value off first).

We have two goals with these heaps:
    1. We want them to be equal in size + or - 1.
    2. We want every value in "small" to be <= every value in "large"

When we want the median, we can simply look at which heap has a greater
length (more elements), and then peek that heap.
If the two heaps have the same length, we can get both and then divide
their sum by two to get the median (still a constant time operation).
"""
import heapq

class Median:
    """
    Note that we're using -1 throughout this class to simulate a maxheap,
    since heapq will be a minheap by default. Multiplying by negative one
    will invert the order and ensure our maxheap behaves as expected.
    """
    def __init__(self) -> None:
        self.small, self.large = [], []

    def insert(self, num: int) -> None:
        # push to maxheap (arbitrarily chosen, just as efficient if
        # we push to minheap first) and swap with minheap if needed
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            # need to swap, largest val in small is bigger than smallest val in large
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        # handle uneven size
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def getMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        # Even # of elements, return avg of two middle nums
        return (-1 * self.small[0] + self.large[0]) / 2


