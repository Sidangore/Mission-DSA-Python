class Solution:
    def getKthFromLast(self, head, k):
        # code here
        front, back = head, head
        for i in range(k):
            if front is None:
                return -1
            front = front.next
        while front is not None:
            back = back.next
            front = front.next
        return back.data
