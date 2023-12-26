class Node:
    """Node object"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List object"""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(5)
    # ll.print()

    ll.traverse_linked_list()
