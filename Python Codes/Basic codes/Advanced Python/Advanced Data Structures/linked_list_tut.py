class Node:
    """Node class"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List class"""

    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, data):
        """inserting at the beginning"""
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link new node to head node
        self.head = new_node

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # Used to add a node to the end of a list

    def append(self, data):
        # create first node if ll is empty
        if self.head is None:
            self.head = Node(data)
            return

        # Traversal ll to tailnode and append
        tail_node = self.head
        while tail_node.next:
            tail_node = tail_node.next

        tail_node.next = Node(data)

    # Used to create a new linked list from a list input
    def append_list(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    def remove_at_index(self, index):
        if index < 0 or index > self.length():
            raise Exception("Index out of range")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Index out of range")

        if index == 0:
            self.insert_at_the_beginning(data)
            return

        new_node = Node(data)
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def insert_after_value(self, value):
        node = Node(value)
        current_node = self.head
        while current_node:
            if current_node.data == value:
                node.next = current_node.next
                current_node.next = node
                # After inserting the new node, move to the next node
                current_node = node.next
            else:
                # If the value doesn't match, continue iterating through the list
                current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_the_beginning(3)
    ll.insert_at_the_beginning(5)
    ll.append(9)
    ll.append_list([1, 3, 4])
    print(ll.length())
    ll.insert_at(1, 4)
    ll.insert_after_value(4)
    ll.print_list()
