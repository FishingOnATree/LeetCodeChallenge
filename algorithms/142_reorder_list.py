# https://leetcode.com/problems/reorder-list/

import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_node(self):
        node = self
        a_list = []
        while node is not None:
            a_list.append(node.val)
            node = node.next
        print(a_list)

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def reorderList(self, head):
        if head is not None:
            node_list = []
            node = head
            while node is not None:
                node_list.append(node)
                node = node.next
            lo = 1
            hi = len(node_list) - 1
            node = head
            while lo < hi:
                node.next = node_list[hi]
                node_list[hi].next = node_list[lo]
                node = node_list[lo]
                lo += 1
                hi -= 1
            if lo == hi:
                node.next = node_list[hi]
                node = node.next
            node.next = None


def convertToList(nums):
    head = None
    node = None
    for n in nums:
        if head is None:
            head = ListNode(n)
            node = head
        else:
            new_node = ListNode(n)
            node.next = new_node
            node = new_node
    return head


MAX_VALUE = 50
a = Solution()
node = convertToList([1, 2, 3, 4, 5, 6, 7, 8])
a.reorderList(node)
node.print_node()
node = convertToList([1, 2, 3, 4, 5, 6, 7])
a.reorderList(node)
node.print_node()
for _ in range(50):
    size = random.randint(0, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [_ for _ in range(size)]
        a_list.sort()
        head = convertToList(a_list)
    print(a_list)
