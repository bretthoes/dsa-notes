"""
HashMap (Associative Array) with Open Addressing

Overview:
- A HashMap (also called a dictionary, map, or associative array) stores key→value pairs
  in (amortized) O(1) time for insert, lookup, and update, by using a hash function to map keys
  to array indices.

Key Concepts:
1. Hashing:
   - We apply a hash function to the key to compute an initial index in an underlying array (buckets).
   - In this simple example, we sum Unicode code points of characters and take modulo capacity.
   - A better real-world hash would be more robust, but this illustrates the idea.

2. Collision Resolution:
   - Collisions occur when two different keys hash to the same index.
   - Here we use **open addressing** with linear probing:
     - If the target bucket is occupied, we move to the next index (wrapping around) until we find
       an empty slot or the existing key.
     - On lookup, we do the same probing sequence to find the key or conclude it’s absent.
   - (Alternative: chaining, where each bucket holds a linked list or another container of entries.)

3. Load Factor & Resizing:
   - We track the number of stored entries (`size`) and the array capacity.
   - To keep probes short and maintain O(1) average performance, we resize (grow) once load factor
     exceeds a threshold (e.g., ≥ 0.5). That is, when size ≥ capacity // 2.
   - On resize, we:
     - Double the capacity.
     - Allocate a new bucket array of length = new capacity, initialized to all None.
     - Re-hash (re-insert) all existing key→value pairs into the new array. Although re-insertion is
       O(old_capacity) work, resizing happens infrequently, so amortized cost remains O(1) per insert.

4. KeyValuePair:
   - A simple container for a key and a value. In this example we restrict keys/values to strings,
     but you could generalize (e.g., use generics or `Any`).

Complexities:
- put / get: O(1) average, O(capacity) worst-case during a rare resize (amortized O(1)).
- Space: O(capacity), which grows roughly double each resize. Total extra memory ~ 2× maximum size before resize.

Collision Resolution Comparison:
1. Chaining:
   - Each bucket holds a list (or linked list) of entries.
   - On collision, append to the chain; lookup scans the chain.
   - Simpler resizing (just increase bucket array, reassign chains), but needs extra memory for lists.
2. Open Addressing (linear probing):
   - No extra per-bucket lists; all entries in one array.
   - Requires careful resizing and deletion handling.
   - May suffer clustering if load factor is high, so keep load ≤ 0.5.
"""

class KeyValuePair:
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value
        
class HashMap:
    """
    Open Addressing HashMap (linear probing) with automatic resizing.
    - Initial capacity: small (e.g., 2), resizes by doubling when size >= capacity//2.
    - Uses a simple string-based hash; replace or improve for other key types.
    - No delete method implemented.
    """
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 2
        # Initialize buckets to None so indexing 0..capacity-1 is valid
        self.map: list[KeyValuePair | None] = [None] * self.capacity

    def _hash_key(self, key: str) -> int:
        """
        Compute hash index for the key in [0..capacity-1].
        Here: sum of code points modulo capacity. For better distribution,
        consider Python's built-in hash: hash(key) % capacity.
        """
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.capacity

    def get(self, key: str) -> str | None:
        """
        Retrieve the value for the given key, or None if absent.
        Probes linearly from the initial hash index until an empty slot.
        """
        i = self._hash_key(key)
        entry = self.map[i]
        while entry is not None:
            # entry is KeyValuePair here
            if entry.key == key:
                return entry.value
            i = (i + 1) % self.capacity
            entry = self.map[i]
        return None

    def put(self, key: str, value: str) -> None:
        """
        Insert or update the key→value pair.
        On inserting a new key, increments size and triggers resize if load factor >= 0.5.
        On updating existing key, just replaces the value.
        """
        i = self._hash_key(key)
        while True:
            entry = self.map[i]
            if entry is None:
                # Empty slot: insert new pair
                self.map[i] = KeyValuePair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif entry.key == key:
                # Key exists: update value
                entry.value = value
                return
            # Otherwise, advance probe
            i = (i + 1) % self.capacity

    def rehash(self) -> None:
        """
        Double capacity, allocate new bucket array, and re-insert all existing entries.
        This keeps load factor low and probe lengths short.
        """
        old_map = self.map
        self.capacity *= 2
        self.map = [None] * self.capacity
        self.size = 0
        for entry in old_map:
            if entry is not None:
                self.put(entry.key, entry.value)


