"""Custom linked list implementation"""


class Node:
    """Create a new node"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Creates an empty linked list"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node to the tail end"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        """Adds a new node before the head node"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """Inserts node after a specified node"""
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """Deletes specified node"""
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None

    def print_list(self):
        """Prints Linked list"""
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(4)
    linked_list.insert_after_node(linked_list.head.next, 5)
    linked_list.delete_node(3)
    linked_list.print_list()
