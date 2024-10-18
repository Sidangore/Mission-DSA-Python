class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MinStack:

    def __init__(self):
        self.head = None
        self.min_num = None

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.min_num = val
            return

        if val >= self.min_num:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        else:
            new_val = (2 * val) - self.min_num
            self.min_num = val
            new_node = Node(new_val)
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> None:
        top_val = self.head.val
        if top_val >= self.min_num:
            deleted_node = self.head
            self.head = self.head.next
            deleted_node.next = None
        else:
            deleted_node = self.head
            self.head = self.head.next
            self.min_num = (2 * self.min_num) - top_val
            deleted_node.next = None

    def top(self) -> int:
        top_val = self.head.val
        if top_val >= self.min_num:
            return top_val
        return self.min_num

    def getMin(self) -> int:
        return self.min_num
