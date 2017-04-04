__author__ = 'Rays'

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a, b = head, head
        for _ in range(n):
            a = a.next
        if a == None:
            head = head.next
        else:
            while a != None and a.next != None:
                a = a.next
                b = b.next
            b.next = b.next.next
        return head