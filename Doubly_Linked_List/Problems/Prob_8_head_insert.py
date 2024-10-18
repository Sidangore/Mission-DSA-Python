def insertInhead(head,data):
    #code here
    new_node = Node(data)
    head.prev = new_node
    new_node.next = head
    return new_node