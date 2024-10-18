
def deleteHead(head):
    #code here
    del_node = head
    head = head.next
    del_node.next = None
    head.prev = None
    return head