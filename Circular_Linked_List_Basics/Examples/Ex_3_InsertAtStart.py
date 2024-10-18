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


def insert_at_start_cll(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    new_node.next = head
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = new_node
    return new_node


def insert_at_start_cll_constant(head, data):
    new_node = Node(data)
    if head is None:
        new_node.next = new_node
        return new_node
    else:
        new_node.next = head.next
        head.next = new_node
        head.data, new_node.data = new_node.data, head.data
    return head


if __name__ == '__main__':
    # Head is None
    head = None
    print_cll(head)

    # Insert 15 at start
    head = insert_at_start_cll_constant(head, 15)
    print_cll(head)

    # Prints only 10
    head = Node(10)
    head.next = head
    print_cll(head)

    # Insert 15 at first, then 20
    head = insert_at_start_cll_constant(head, 15)
    head = insert_at_start_cll_constant(head, 20)
    print_cll(head)




