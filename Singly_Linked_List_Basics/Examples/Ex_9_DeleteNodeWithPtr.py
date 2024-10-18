class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


# Assumption: ptr shouldn't be last node
def delete_ptr(ptr):
    ptr.key = ptr.next.key
    ptr.next = ptr.next.next


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

    head2 = t2
    print_list(head2)

    # delete_ptr(t4) # Assumption: Ptr shouldn't be last node
    delete_ptr(t2)

    print_list(t2)  # 30 50
    print_list(head)  # 10 30 50
