class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        curr = head
        prev = None
        while curr:
            prev = curr
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev
        return prev