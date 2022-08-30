class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_dummy = ListNode()
        even_dummy = ListNode()
        temp_odd = odd_dummy
        temp_even = even_dummy
        odd = True
        while head:
            if odd:
                odd_dummy.next = head
                head = head.next
                odd_dummy = odd_dummy.next
                odd = False
            else:
                even_dummy.next = head
                head = head.next
                odd_dummy = even_dummy.next
                odd = True
        odd_dummy.next = temp_even.next
        return temp_odd.next

