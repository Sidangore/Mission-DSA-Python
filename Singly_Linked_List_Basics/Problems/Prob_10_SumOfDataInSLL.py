def sumOfElements(head):
    # code here
    res = 0
    curr = head
    while curr is not None:
        res += curr.data
        curr = curr.next
    return res
