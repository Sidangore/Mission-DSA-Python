class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def nth_from_end(head, n):
    # Negative N places cannot be printed
    if n < 1:
        print(f"{n}th from end cannot be printed")
        return

    # S.L.L is Empty
    if head is None:
        print("S.L.L is Empty")
        return

    fast, slow = head, head

    # Move fast pointer N places ahead
    for i in range(n):

        # If fast reaches end, i.e. N is out of range
        if fast is None:
            print(f"{n}th from end cannot be printed, out of range")
            return

        # Move fast
        fast = fast.next

    # Move fast and slow by one node till fast reaches the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # Nth from the end is pointed by slow
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

    # Nth from end
    nth_from_end(head, 1)
    nth_from_end(head, 0)
    nth_from_end(head, 2)
    nth_from_end(head, 3)
    nth_from_end(head, 4)
    nth_from_end(head, 5)

