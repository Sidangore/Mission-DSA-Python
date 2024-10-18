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

    def insertAtStart(self, x):
        new_node = Node(x)
        new_node.next = self
        return new_node

    def insertAtEnd(self, x):
        if self is None:
            return Node(x)
        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(x)
        return self


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
    head = head.insertAtStart(40)
    head = head.insertAtStart(60)
    head.print_list()
    print(head.search(40))
    head.insertAtEnd(60)
    head.insertAtEnd(70)
    head.print_list()
    print(head.search(70))

    

