# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2, remainder=0, cache={}):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll_sum = l1.val if l1 is not None else 0
        ll_sum += l2.val if l2 is not None else 0
        if ll_sum < 10:
            new_node = ListNode(val=ll_sum, next=self.addTwoNumbers(l1.next, l2.next))
        else:
            new_node = ListNode(
                val=ll_sum % 10, next=self.addTwoNumbers(l1.next, l2.next, remainder=1)
            )
        if "head_node" not in cache.keys():
            cache["head_node"] = new_node
        if l1 is None and l2 is None:
            return cache.get("head_node")


if __name__ == "__main__":
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    # link them
    a.next = b
    b.next = c
    c.next = None

    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(4)
    # Link them
    d.next = e
    e.next = f
    f.next = None

    print(Solution().addTwoNumbers(l1=a, l2=b))
