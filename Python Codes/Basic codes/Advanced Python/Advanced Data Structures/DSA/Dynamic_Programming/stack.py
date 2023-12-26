class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(head):
    ll_list = []
    while head:
        ll_list.append(head.val)
        head = head.next
    print(ll_list)


def push(data, top=None):
    new_node = Node(data)
    new_node.next = top
    return new_node


def pop(head):
    if head is None:
        return "Stack overflow"
    curr = head.next
    head.next = None
    return curr


# Sample Nodes
a = Node(5)
b = Node(6)

a.next = b

# print_ll(push(5, a))
# print_ll(push(9, push(5, a)))
# print_ll(pop(push(9, push(5, a))))
