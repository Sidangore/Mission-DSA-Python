class Node:
    def __init__(self, x):
        self.key = x
        self.next = None


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


def insert(head, pos, x):
    node = Node(x)
    if pos == 1:
        node.next = head
        return node
    curr = head
    for i in range(pos - 2):
        curr = curr.next
        if curr is None:
            return head
    node.next = curr.next
    curr.next = node
    return head


if __name__ == '__main__':
    t1 = Node(10)
    t2 = Node(20)
    t3 = Node(30)
    t4 = Node(50)
    head = t1
    head.next = t2
    head.next.next = t3
    head.next.next.next = t4
    print_list(head)
    head = insert(head, 3, 80)
    print_list(head)
    head = insert(head, 1, 8)
    print_list(head)
    head = insert(head, 10, 88)
    print_list(head)
    head = insert(head, 6, 88)
    print_list(head)
    head = insert(head, 8, 98)
    print_list(head)
    head = insert(head, 10, 100)
    print_list(head)