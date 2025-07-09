"""
In some scenarios, we may require two heaps for an optimal algorithm.

Example:
Imagine a Median finder, where you simply need to find the median of a list.
But, you aren't provided the list up front, but rather as a stream of values.
The values are not in sorted order, and you still need to be able to return
the median when requested, but also account for new unsorted values to the
structure that may be added later.

We need to:
- Insert new values into sorted order
- Return the median of the current list of values when requested

Naively, we could get the median by using half the length of the array,
and returning the value at  that index (or the average of the two values
if the list is even in length). 
When we get a new value, we could iterate through our list each time to
find the correct ordered position for the new number.
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
"""
 



