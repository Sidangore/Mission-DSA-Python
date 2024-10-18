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


def delete_head(head):
    if head is None or head.next is None:
        return None

    next_node = head.next
    head.next = None
    next_node.prev = None

    return next_node


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
    head = delete_head(head)
    print("After Insertion 11 head in D.L.L: ", end=" ")
    print_dll(head)

    head2 = None
    head2 = delete_head(head2)
    print("After Insertion 11 head in Empty D.L.L: ", end=" ")
    print_dll(head2)
