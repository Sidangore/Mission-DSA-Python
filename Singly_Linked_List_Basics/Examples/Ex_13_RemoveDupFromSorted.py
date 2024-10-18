class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def remove_duplicates(head):
    curr = head

    # Compare the curr and the next node
    while curr is not None and curr.next is not None:

        # Remove the next duplicate until all duplicates are over except one
        if curr.key == curr.next.key:
            curr.next = curr.next.next

        else:
            # This is under else because if there are more the 3 duplicates,
            # we only need to keep one
            curr = curr.next


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
    t1.next = Node(10)
    t1.next.next = Node(10)
    t2 = Node(20)
    t3 = Node(20)
    t4 = Node(30)
    t4.next = Node(30)
    t4.next.next = Node(30)
    head = t1.next.next
    head.next = t2
    head.next.next = t3
    head.next.next.next = t4

    # Original List
    print_list(head)

    # Remove Duplicates
    remove_duplicates(head)
    print_list(head)
