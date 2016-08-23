# https://leetcode.com/problems/partition-list/
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
    def partition(self, head, x):
        if head is None:
            return None
        else:
            node = head
            ltx_head = None
            ltx_tail = None
            getx_head = None
            getx_tail = None
            while node is not None:
                this_node = node
                node = node.next
                if this_node.val < x:
                    if ltx_head is None:
                        ltx_head = this_node
                        ltx_tail = this_node
                    else:
                        ltx_tail.next = this_node
                        ltx_tail = this_node
                else:
                    if getx_head is None:
                        getx_head = this_node
                        getx_tail = this_node
                    else:
                        getx_tail.next = this_node
                        getx_tail = this_node
                this_node.next = None
            if ltx_head is None:
                return getx_head
            else:
                ltx_tail.next = getx_head
                return ltx_head


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
# a.partition(convertToList([2, 4, 6, 8, 1, 3, 5, 6]), 0).print_node()
# a.partition(convertToList([2, 4, 6, 8, 1, 3, 5, 6]), 10).print_node()
# a.partition(convertToList([2, 4, 6, 8, 1, 3, 5, 6]), 4).print_node()
# a.partition(convertToList([2, 4, 6, 8, 1, 3, 5, 6]), 5).print_node()
for _ in range(25):
    size = random.randint(0, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [random.randint(0, MAX_VALUE) for _ in range(size)]
    print(a_list)
    print(random.randint(0, MAX_VALUE))
    #print("Original: ", head.print_node())
    #print("Updated:", a.oddEvenList(head).print_node())