class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def print_dll(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    
    return head


if __name__ == '__main__':
    head = Node(10)
    temp1 = Node(20)
    temp2 = Node(30)

    head.next = temp1
    temp1.prev = head

    temp1.next = temp2
    temp2.prev = temp1

    # Print D.L.L of 3 Nodes
    print("Initial D.L.L: ", end=" ")
    print_dll(head)

    # Ex. 1. Insert 11
    head = insert_end(head, 11)
    print("After Insertion 11 head in D.L.L: ", end=" ")
    print_dll(head)

    head2 = None
    head2 = insert_end(head2, 11)
    print("After Insertion 11 head in Empty D.L.L: ", end=" ")
    print_dll(head2)
