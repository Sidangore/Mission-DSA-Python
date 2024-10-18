class Node:
    def __init__(self, x):
        self.key = x
        self.next = None

    def print_list(self):
        curr = self
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.next
        print()

    def search(self, x):
        curr = self
        pos = 1
        while curr is not None:
            if curr.key == x:
                return pos
            pos += 1
            curr = curr.next
        return -1


if __name__ == '__main__':
    t1 = Node(10)
    t2 = Node(20)
    t3 = Node(30)
    t4 = Node(50)
    head = t1
    head.next = t2
    head.next.next = t3
    head.next.next.next = t4
    head.print_list()
    print(head.search(40))
    print(head.search(30))
