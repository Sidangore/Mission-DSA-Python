def maximum(head):
    # code here
    res = head.data
    curr = head.next
    while curr is not None:
        if curr.data > res:
            res = curr.data
        curr = curr.next
    return res


def minimum(head):
    # code here
    res = head.data
    curr = head.next
    while curr is not None:
        if curr.data < res:
            res = curr.data
        curr = curr.next
    return res
