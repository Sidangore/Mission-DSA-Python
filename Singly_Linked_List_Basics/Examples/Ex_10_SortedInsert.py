class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def sorted_insert(head, value):
    # Allocate new node for value
    new_node = Node(value)

    # S.L.L is empty
    if head is None:
        return new_node

    # Value is smaller than the first node, hence inserted at the start
    elif value < head.key:
        new_node.next = head
        return new_node

    # Value's is lying in between (or) at last of S.L.L
    curr = head

    # Stop if we reach the end (or) value is greater the next's key
    while curr.next is not None and curr.next.key < value:
        curr = curr.next

    # Insert the new node
    new_node.next = curr.next
    curr.next = new_node

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
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

    print_list(head)

    head = sorted_insert(head, 15)
    print_list(head)

    head = sorted_insert(head, 45)
    print_list(head)

    head = sorted_insert(head, 5)
    print_list(head)

    head = sorted_insert(head, 75)
    print_list(head)
