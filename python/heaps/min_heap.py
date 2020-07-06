class MinHeap(object):
    NOT_FOUND = -1

    def __init__(self, potential_heap=None):
        self.heap = potential_heap
        if not isinstance(self.heap, list):
            raise TypeError(f"Needs to be a list, instead found {repr(self.heap)}")

        # heapifying list, iterating backwards
        for idx in range(len(self.heap) - 1, -1, -1):
            self.__bubble_down(idx)

    @classmethod
    def sort(cls, unsorted_list):
        sorted_list = []
        min_heap = cls(unsorted_list)
        while not min_heap.empty():
            smallest_item = min_heap.pop()
            sorted_list.append(smallest_item)

        return sorted_list

    def pop(self):
        smallest = self.heap[0]
        self.__swap(0, self.__last_idx())
        self.heap.pop()
        self.__bubble_down(0)

        return smallest

    def peek(self):
        return self.heap[0]

    def push(self, num):
        self.heap.append(num)
        self.__bubble_up(self.__last_idx())

    def bubble_down(self, idx):
        return self.__bubble_down(idx)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.heap)

    # alias for size
    def count(self):
        return self.size()

    # alias for size
    def length(self):
        return self.size()

    def __bubble_down(self, idx):
        if self.__out_of_bounds(idx):
            return self.NOT_FOUND

        left_child_idx = self.__left_child_position(idx)
        right_child_idx = self.__right_child_position(idx)
        while left_child_idx != -1 or right_child_idx != -1:
            n = self.heap[idx]
            # left and right children both exist
            if left_child_idx != -1 and right_child_idx != -1:
                left_child = self.heap[left_child_idx]
                right_child = self.heap[right_child_idx]

                # both children are larger than you. you're at the right place
                if right_child >= n and left_child >= n:
                    break

                # one of the children is larger than you. pick the smaller one
                if right_child > n and left_child <= n:
                    idx_to_swap = left_child_idx
                elif right_child < n and left_child >= n:
                    idx_to_swap = right_child_idx
                # both children are smaller than you. pick the smallest one
                elif left_child <= right_child:
                    idx_to_swap = left_child_idx
                elif right_child <= left_child:
                    idx_to_swap = right_child_idx
            # only left child exists and is smaller
            elif left_child_idx != -1 and self.heap[left_child_idx] < n:
                idx_to_swap = left_child_idx
            # only right child exists and is smaller
            elif right_child_idx != -1 and self.heap[right_child_idx] < n:
                idx_to_swap = right_child_idx
            else:
                break

            self.__swap(idx, idx_to_swap)

            idx = idx_to_swap
            left_child_idx = self.__left_child_position(idx)
            right_child_idx = self.__right_child_position(idx)

        return idx

    def __bubble_up(self, idx):
        if self.__out_of_bounds(idx):
            return self.NOT_FOUND

        parent_idx = self.__parent_position(idx)
        while parent_idx != -1:
            if self.heap[idx] < self.heap[parent_idx]:
                self.__swap(idx, parent_idx)
                idx = parent_idx
                parent_idx = self.__parent_position(idx)
            else:
                break

        return idx

    def __parent_position(self, idx):
        if idx == 0:
            return self.NOT_FOUND

        pos = (idx - 1) // 2
        if self.__out_of_bounds(pos):
            return self.NOT_FOUND

        return pos

    def __right_child_position(self, idx):
        pos = (idx * 2) + 2
        if self.__out_of_bounds(pos):
            return self.NOT_FOUND

        return pos

    def __left_child_position(self, idx):
        pos = (idx * 2) + 1
        if self.__out_of_bounds(pos):
            return self.NOT_FOUND

        return pos

    def __num_of_layers(self):
        return len(self.heap) // 2

    def __out_of_bounds(self, idx):
        return idx >= self.__num_of_nodes() or idx < 0

    def __num_of_nodes(self):
        return len(self.heap)

    def __swap(self, idx1, idx2):
        if self.__out_of_bounds(idx1):
            raise ValueError(f"{idx1} is out of heap bounds")

        if self.__out_of_bounds(idx2):
            raise ValueError(f"{idx2} is out of heap bounds")

        temp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = temp

    def __last_idx(self):
        return len(self.heap) - 1
