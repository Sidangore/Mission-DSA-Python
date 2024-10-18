
def insertInTail(head,data):
    #code here
    curr = head
    while curr.next is not None:
        curr = curr.next
    new_node = Node(data)
    curr.next = new_node
    new_node.prev = curr
    return head