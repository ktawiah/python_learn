from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_array(size: int) -> List[ListNode]:
    return [ListNode(0) for num in range(size)]


def _hash(data, size: int) -> int:
    if isinstance(data, int):
        return data % size

    if isinstance(data, str):
        key = ""
        for char in data:
            key += str(ord(char))

        return int(key) % size


def add(data) -> None:
    list_array = create_array(50)
    key = _hash(data, 50)
    new_node = ListNode(data)
    head = list_array[key]
    while head:
        if head.val == data:
            break

        if head.next is None:
            head.next = new_node
            break

        head = head.next

    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    print(add("Walker"))
    print(add("Kelvin"))
