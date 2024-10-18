'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def deleteAtPosition(head, pos):
    # code here
    if head is None:
        return None
    if pos == 1:
        head = head.next
        return head
    curr = head
    for i in range(pos - 2):
        if curr is None:
            return head
        curr = curr.next
    curr.next = curr.next.next
    return head
