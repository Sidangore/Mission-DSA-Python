'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def deleteHead(head):
    # code here
    if head is None:
        return None
    temp = head.next
    head.next = None
    return temp
