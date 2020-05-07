import heapq


class MinPriorityQueue(object):
    def __init__(self, heap=None):
        if heap is None:
            heap = []

        self.heap = heap

    def append(self, val):
        heapq.heappush(self.heap, val)
        return val

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap)
