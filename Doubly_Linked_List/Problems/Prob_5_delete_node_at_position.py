class Solution:
    def delete_node(self, head, x):
        #code here
        if x == 1:
            head = head.next
            head.prev = None
            return head
        curr = head
        for _ in range(x - 2):
            curr = curr.next
        curr.next = curr.next.next
        if curr.next:
            curr.next.prev = curr
        return head