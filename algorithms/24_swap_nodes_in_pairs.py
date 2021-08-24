# https://leetcode.com/problems/swap-nodes-in-pairs/#/description

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        curr = self
        values = list()
        while curr is not None:
            values.append(str(curr.val))
            curr = curr.next
        return " ".join(values)

    def get_values(self):
        curr = self
        values = list()
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        return values


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        old_head = head
        a = head.next.next
        head = head.next
        head.next = old_head
        old_head.next = a
        while a and a.next:
            print()
        return head
