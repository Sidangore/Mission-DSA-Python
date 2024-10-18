import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def peek(self):
        if self.head is None:
            return sys.maxsize
        return self.head.data

    def length(self):
        return self.size

    def pop(self):
        if self.head is None:
            return sys.maxsize
        deleted_node = self.head
        self.head = self.head.next
        deleted_node.next = None
        self.size -= 1
        return deleted_node.data

    def print(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def is_empty(self):
        return self.head is None


if __name__ == '__main__':
    s = MyStack()

    s.push(10)
    s.push(20)
    s.push(30)

    s.print()

    s.pop()
    print(s.peek())

    s.pop()
    s.print()

    print(s.peek())

    print(s.length())
    print(s.is_empty())

    s.pop()
    print(s.is_empty())
