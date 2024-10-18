class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        curr = head
        prev, temp = None, None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
