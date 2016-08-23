# https://leetcode.com/problems/reverse-linked-list-ii/

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
    def reverseBetween(self, head, m, n):
        if head is None or n == 0 or m == n:
            return head
        else:
            count = 1
            node = head
            if m > 1:
                while count < m - 1:
                    count += 1
                    node = node.next
                # node at m-1 element
                bridge_node = node
                node = node.next
                count += 1
            else:
                node = head
                bridge_node = None
            reverse_head = node
            reverse_tail = node
            while count <= n:
                reverse = node
                node = node.next
                count += 1
                reverse.next = reverse_head
                reverse_head = reverse
            if bridge_node is None:
                return_node = reverse_head
            else:
                return_node = head
                bridge_node.next = reverse_head
            reverse_tail.next = node
            return return_node


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
a.reverseBetween(node, 1, 3).print_node()
node = convertToList([1, 2, 3, 4, 5, 6, 7])
a.reverseBetween(node, 5, 7).print_node()
for _ in range(50):
    size = random.randint(1, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [_ for _ in range(size)]
        a_list.sort()
    print(a_list)
    n = random.randint(1, size)
    m = random.randint(1, size)
    print(min(n, m))
    print(max(n, m))

