class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insertInMiddle(self, head, x):
        # code here

        new_node = Node(x)

        if head is None:
            return new_node

        fast, slow = head.next, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        new_node.next = slow.next
        slow.next = new_node
        return head
