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


def reverse_dll(head):
    if head is None or head.next is None:
        return None

    curr = head
    prev = None
    while curr is not None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev

    return prev


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
    head = reverse_dll(head)
    print("After Reversing D.L.L: ", end=" ")
    print_dll(head)

