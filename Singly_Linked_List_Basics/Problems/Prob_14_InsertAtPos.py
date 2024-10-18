def insertAtPosition(head, pos, data):
    # code here
    new_node = Node(data)
    if head is None:
        return None
    curr = head
    for _ in range(pos - 1):
        if curr.next is None:
            return head
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
    return head
