from collections import deque  # linked list


class LRUCache(object):
    def __init__(self, max_capacity=30):
        self.max_capacity = max_capacity
        # linkedlist holding order of keys
        # first item (index 0) is most recently used, last item is least recently used
        self.counter = deque([])
        # actual items stored here
        self.cache = {}

    def __str__(self):
        return f"{str(self.cache)}, eviction order {str(self.counter)}"

    def __len__(self):
        return len(self.counter)

    def get(self, key):  # O(1) + O(n)
        if key not in self.cache:
            return None

        self.mark_most_recent(key)
        return self.cache[key]

    def has(self, key):
        # check if item is in a cache without moving it's order
        return key in self.cache

    def set(self, key, value):
        # if the cache already has the item, move it to the front instead
        if key in self.cache:
            self.mark_most_recent(key)
            return

        # if the cache is full, evict the least recently used item
        if self.full():
            least_recently_used_key = self.counter.pop()
            del self.cache[least_recently_used_key]

        self.counter.appendleft(key)
        self.cache[key] = value

    def mark_most_recent(self, key):  # O(n) because deque is a doubly linkedlist
        # find and pluck the key in deque
        try:
            removed_val = self.counter.remove(key)
        except ValueError:
            return
        # append key to the front of the deque to mark it as most
        # recently read element
        # also pushes every single element with index higher than
        # plucked key by order down by 1
        self.counter.appendleft(removed_val)

    def full(self):
        return self.max_capacity == len(self.counter)
