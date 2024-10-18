from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_cll(head: Optional[Node]):
    if head is None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def insert_at_end_cll_constant(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
    else:
        new_node.next = head.next
        head.next = new_node
        head.data, new_node.data = new_node.data, head.data
    return new_node


if __name__ == '__main__':
    # Head is None
    head = None
    print_cll(head)

    # Insert 15 at start
    head = insert_at_end_cll_constant(head, 15)
    print_cll(head)

    # Prints only 10
    head = Node(10)
    head.next = head
    print_cll(head)

    # Insert 15 at end, then 20
    head = insert_at_end_cll_constant(head, 15)
    print_cll(head)
    head = insert_at_end_cll_constant(head, 20)
    print_cll(head)




