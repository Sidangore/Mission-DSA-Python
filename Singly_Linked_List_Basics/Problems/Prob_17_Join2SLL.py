'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def joinTheLists(head1, head2):
    # code here
    curr = head1
    while curr.next is not None:
        curr = curr.next
    curr.next = head2
    return head1
