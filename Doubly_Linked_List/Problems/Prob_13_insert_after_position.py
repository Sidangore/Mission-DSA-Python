class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
        new_node = Node(x)
        curr = head
        for _ in range(p):
            curr = curr.next
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        return head