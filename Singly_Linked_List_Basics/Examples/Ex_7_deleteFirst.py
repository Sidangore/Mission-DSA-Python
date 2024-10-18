class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def delete_start(head):
    if head is None:
        return None
    else:
        return head.next

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
    head = delete_start(head)
    print_list(head)
    head = delete_start(None)
    print_list(head)