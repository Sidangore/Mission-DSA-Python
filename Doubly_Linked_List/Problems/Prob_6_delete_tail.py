"""
We have to go to end of DLL because its not Circular
"""
def deleteTail(head):
    #code here
    curr = head
    while curr.next is not None:
        curr = curr.next
    tail = curr.prev
    tail.next = None
    return head