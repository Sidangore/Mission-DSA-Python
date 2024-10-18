class Solution:
    def compareCLL(self, head1, head2):
        # code here
        tail1, tail2 = head1.prev, head2.prev

        if tail1.data != tail2.data:
            return False

        while tail1 != head1 and tail2 != head2:
            if tail1.data != tail2.data:
                return False
            tail1 = tail1.prev
            tail2 = tail2.prev

        return tail1 == head1 and tail2 == head2