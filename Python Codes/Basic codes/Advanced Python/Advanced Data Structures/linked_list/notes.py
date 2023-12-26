from time import time


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# In order to create a linked list, you need to create instances of the node, and link them using the next pointer

node_a = Node(5)
node_b = Node(6)
node_c = Node(7)
node_d = Node(8)

# Link them
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d


# Iterative implementation traversal
def traverse(head):
    start_time = time()
    current = head
    while current.next is not None:
        print(current.data)
        current = current.next
    end_time = time()
    print(end_time - start_time)


# Recursive implementation of the traversal
# If you access the data before the recursive function the linked list is reversed...Nice!!
def traverse_rec(head):
    # First check your base case(the point where the recursion terminates)
    if head is None:
        return
    traverse_rec(head.next)
    print(head.data)


ll_list = []


def ll_to_list(head):
    # Traverse through ll
    if head is None:
        return

    ll_list.append(head.data)
    ll_to_list(head.next)

    # traverse_rec(node_a)
    # ll_to_list(node_a)
    # print(ll_list)


def sum_of_ll(head):
    # traverse ll
    current = head
    if current is None:
        return 0
    return current.data + sum_of_ll(current.next)


def search_ll(head, target):
    current = head
    if current is None:
        return False

    if current.data == target:
        return True

    return search_ll(current.next, target)


def value_at_index(head, index):
    if head is None:
        return None
    if index == 0:
        return head.data
    return value_at_index(head.next, index - 1)


def reverse_ll(head, prev=None):
    if head is None:
        return prev

    head.next = prev
    return reverse_ll(head.next, head)


# print(value_at_index(node_a, 2))
# print(search_ll(node_a, 7))
