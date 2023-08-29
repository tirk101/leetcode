class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len_linkedlist = 1
        cur = head
        while cur.next: cur, len_linkedlist = cur.next, len_linkedlist + 1
        if len_linkedlist - n == 0: return head.next
        cur = head
        count = 1
        while count != len_linkedlist - n: cur, count = cur.next, count + 1
        temp = cur.next
        cur.next = temp.next
        return head 
