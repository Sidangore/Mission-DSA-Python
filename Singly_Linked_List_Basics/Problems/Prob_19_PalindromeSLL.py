class Solution:
    def reverseSLL(self, head):
        curr = head
        prev = None
        temp = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self, head):
        # code here
        ptr1, ptr2 = head, head.next

        while ptr2 is not None and ptr2.next is not None:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next

        ptr1 = ptr1.next
        ptr1 = self.reverseSLL(ptr1)
        ptr2 = head

        while ptr1 is not None:
            if ptr2.data != ptr1.data:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True
