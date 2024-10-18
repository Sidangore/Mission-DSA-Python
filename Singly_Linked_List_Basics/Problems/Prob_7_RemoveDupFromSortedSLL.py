def removeDuplicates(head):
    #code here
    curr = head
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next