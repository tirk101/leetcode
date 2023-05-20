 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def list2num(l):
            num = ""
            while l:
                num = str(l.val) + num
                l = l.next
            return int(num)
        num = list2num(l1) + list2num(l2)
        cur = root = ListNode(0)
        for i in str(num)[::-1]:
            cur.next = ListNode(int(i))
            cur = cur.next
        print(root.next)
        return root.next
