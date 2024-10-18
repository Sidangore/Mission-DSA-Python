class Solution:
    def isCircular(self, head):
        #code here
        tail = head.prev
        while tail is not None and head is not None:
            if tail == head:
                return True
            tail = tail.prev
            head = head.next
        return False