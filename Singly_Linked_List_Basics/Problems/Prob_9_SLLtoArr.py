def displayList(head):
    # code here
    arr = []
    while head is not None:
        arr.append(head.data)
        head = head.next
    return arr
