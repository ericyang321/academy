class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, existing_data=None):
        self.head = None
        if existing_data is not None:
            self.insert_multiple(existing_data)

    def __getitem__(self, index):
        n = self.traverse_to_node(index)
        if n is not None:
            return n.data

    def __str__(self):
        n = self.head
        str_representation = ""
        while n is not None:
            str_representation += f"{n.data} -> "
            n = n.next

        return str_representation

    def traverse_to_node(self, index):
        n = self.head
        while index > 0:
            if n is None:
                break

            n = n.next
            index -= 1

        if n is None:
            return None

        return n

    def remove_at(self, index):
        if index == 0:
            self.head.next = None
            return

        prev_node = self.traverse_to_node(index - 1)
        if prev_node is None or prev_node.next is None:
            raise Exception(f"Node at {index} does not exist")

        to_be_deleted_node = prev_node.next
        next_node = to_be_deleted_node.next

        prev_node.next = next_node
        to_be_deleted_node.next = None

    def insert_multiple(self, data_list):
        start_index = 0
        n = self.find_tail_node()
        if n is None:
            self.head = Node(data_list[0])
            n = self.head
            start_index = 1

        for i in range(start_index, len(data_list)):
            data = data_list[i]
            n.next = Node(data)
            n = n.next

    def find_tail_node(self):
        n = self.head
        if n is None:
            return None

        while n.next is not None:
            n = n.next

        return n

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return self.head

        tail = self.find_tail_node()
        tail.next = Node(data)
        return tail.next

