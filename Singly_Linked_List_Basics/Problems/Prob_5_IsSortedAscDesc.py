# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def isSorted(head):
    # One 1 node present, then its always sorted
    if head.next is None:
        return 1

    curr = head

    # Initially, assuming that array is sorted in ascending or descending
    asc = True
    desc = True

    # To compare, curr.next shouldn't be None (curr and curr.next)
    while curr.next is not None:
        if curr.data < curr.next.data:  # This means, it isn't descending
            desc = False
        if curr.data > curr.next.data:  # This means, it isn't ascending
            asc = False
        curr = curr.next  # Moving curr forward till the last node

    if asc:  # If asc tag was never False, it would have been sorted in pure ascending order
        return 1
    if desc:  # If desc tag was never False, it would have been sorted in pure descending order
        return 1

    # Neither of above is True, i.e. S.L.L is neither ascending nor descending
    return 0
