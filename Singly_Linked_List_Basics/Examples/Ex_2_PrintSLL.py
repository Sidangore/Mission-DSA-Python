class Node:
    def __init__(self, x):
        self.key = x
        self.next = None

    # def printList(head):
    #     curr = head
    #     while curr is not None:
    #         print(curr.key, end=" ")
    #         curr = curr.next
    def printList(self):
        curr = head
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.next


if __name__ == '__main__':
    t1 = Node(10)
    t2 = Node(20)
    t3 = Node(30)
    head = t1
    head.next = t2
    head.next.next = t3
    head.printList()
    