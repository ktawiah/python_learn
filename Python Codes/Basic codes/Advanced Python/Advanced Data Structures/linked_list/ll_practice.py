from itertools import combinations
from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_middle(head, n, new_node):
    current = head
    if current is None:
        return

    if n == 1:
        next_node = current.next
        current.next = new_node
        new_node.next = next_node

    insert_at_middle(current.next, n - 1, new_node)


def delete_beginning_node(head):
    next_node = head.next
    head.next = None
    return next_node


def delete_at_end(head):
    current = head
    if current.next.next is None:
        # tail = current.next
        current.next = None
        return
    delete_at_end(head.next)


def print_ll(head):
    if head is None:
        return

    print(head.data, end="->")
    print_ll(head.next)


a1 = Node(1)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)

# link them
a1.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = None

# insert_at_middle(a1, 2, Node(7))
# delete_beginning_node(a1)
delete_at_end(a3)
print_ll(a3)


# def b_search(nums: List[int], target: int, left=0, right=len(nums) - 1) -> int:
#     """Search for a number in a list using BS algorithm

#     Parameters
#     ----------
#     nums : List[int]
#         List of numbers
#     target : int
#         Target value to search for

#     Returns
#     -------
#     int
#         Index of number in list
#     """
#     if left == right:
#       return left
