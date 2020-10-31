import heapq


class MinPriorityQueue(object):
    def __init__(self, heap):
        self.heap = heap

    def append(self, elem):
        heapq.heappush(self.heap, elem)
        return elem

    def pop(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)
