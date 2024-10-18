class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def get_middle(head):
    # S.L.L is empty
    if head is None:
        return

    fast, slow = head, head

    # Move forward till fast is None, for Even number of nodes
    # Move forward till fast is Last Node, for Odd number of nodes
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Slow will be the middle element of S.L.L after fast reaches its end
    print(slow.key)


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

    # Original List
    print_list(head)

    # Prints the middle element of S.L.L
    get_middle(head)
