#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        #code here
        new_node = Node(x)
        if head.data >= x:
            new_node.next = head
            head.prev = new_node
            return new_node
        else:
            curr = head
            while curr.next:
                if curr.next.data >= x:
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                    new_node.prev = curr
                    return head
                else:
                    curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            return head