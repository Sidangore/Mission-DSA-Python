class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    head = Node(10)
    head.next = Node(5)
    head.next.next = Node(15)
    head.next.next.next = Node(20)
    head.next.next.next.next = head
