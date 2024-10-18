def displayList(head):
    #code here
    arr = []
    arr.append(head.data)
    curr = head.next
    while curr:
        arr.append(curr.data)
        curr = curr.next
    return arr