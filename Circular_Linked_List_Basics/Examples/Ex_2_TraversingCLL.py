from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_cll(head: Optional[Node]) -> None:
    if head is None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


def print_cll_2(head: Optional[Node]) -> None:
    if head is None:
        return
    curr = head
    while curr.next != head:
        print(curr.data, end=" ")
        curr = curr.next
    print(curr.data)


if __name__ == '__main__':
    head = None
    print_cll_2(head)

    head = Node(10)
    head.next = head
    print_cll_2(head)

    head.next = Node(5)
    head.next.next = Node(15)
    head.next.next.next = Node(20)
    head.next.next.next.next = head

    print_cll_2(head)

