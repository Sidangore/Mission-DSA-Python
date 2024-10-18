#User function Template for python3

class Solution:
    def findMiddle(self, head):
        #code here
        fast, slow = head.next, head
        while fast != head:
            fast = fast.next.next
            slow = slow.next
        return slow.data