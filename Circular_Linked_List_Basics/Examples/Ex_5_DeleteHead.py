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


def delete_head_constant(head):
    if head is None or head.next == head:
        return None
    head.data, head.next.data = head.next.data, head.data
    head.next = head.next.next
    return head


if __name__ == '__main__':
    # Head is None
    head = None
    print_cll(head)

    head = delete_head_constant(head)
    print_cll(head)

    head = Node(10)
    head.next = head
    print_cll(head)

    # Delete 10 at start
    head = delete_head_constant(head)
    print_cll(head)

    # Delete only 10
    head = Node(10)
    head.next = Node(15)
    head.next.next = head

    head = delete_head_constant(head)
    print_cll(head)

    head = Node(10)
    head.next = Node(15)
    head.next.next = Node(20)
    head.next.next.next = head
    head = delete_head_constant(head)
    print_cll(head)






