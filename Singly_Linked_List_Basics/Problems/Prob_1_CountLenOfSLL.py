'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        curr = head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        return count
