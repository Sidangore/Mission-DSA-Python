class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def reverse_sll(head):
    # 3 pointers
    behind = None
    curr = head
    ahead = None

    while curr is not None:
        ahead = curr.next  # Set the next node
        curr.next = behind  # Reverse the curr's next to prev
        behind = curr  # Move prev to curr
        curr = ahead  # Move curr to next node

    # Return behind as this is the First Node in reversed S.L.L
    return behind


def print_list(head):
    print("Head->", end=" ")

    # Starting point for curr
    curr = head

    # Print and Move till curr is not at end
    while curr is not None:
        print(curr.key, end=" -> ")
        curr = curr.next

    print("None")


if __name__ == '__main__':
    t1 = Node(10)
    t2 = Node(40)
    t3 = Node(20)
    t4 = Node(30)
    t4.next = Node(30)
    t4.next.next = Node(30)
    head = t1
    head.next = t2
    head.next.next = t3
    head.next.next.next = t4

    # Original List
    print_list(head)

    # Reverse S.L.L
    head = reverse_sll(head)
    print_list(head)
