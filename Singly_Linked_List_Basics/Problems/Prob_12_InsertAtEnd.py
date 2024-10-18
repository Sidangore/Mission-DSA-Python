class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        new_node = Node(x)
        if head is None:
            return new_node
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        return head
