class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def insert_sorted(head, x):
    new_node = Node(x)
    if head is None:
        return new_node
    if x < head.data:
        new_node.next = head
        return new_node
    curr = head
    while curr.next is not None and curr.next.data < x:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == '__main__':
    t1 = Node(10)
    t2 = Node(20)
    t3 = Node(30)
    t4 = Node(50)
    head = t1
    head.next = t2
    head.next.next = t3
    head.next.next.next = t4

    # Original List
    print_list(head)

    # Insert in sorted S.L.L
    head = insert_sorted(head, 15)
    print_list(head)
