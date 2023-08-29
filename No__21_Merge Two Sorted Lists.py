class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val :
                cur.next = cur = list1
                list1 = list1.next
            else:
                cur.next = cur = list2
                list2 = list2.next
        if list1: cur.next = list1
        elif list2: cur.next = list2
        return dummy.next
