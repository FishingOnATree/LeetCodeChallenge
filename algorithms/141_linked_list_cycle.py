# https://leetcode.com/problems/odd-even-linked-list/
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
    def detectCycle(self, head):
        check_set = set()
        node = head
        while node is not None and node not in check_set:
            check_set.add(node)
            node = node.next
        return node


def convertToList(nums, loop_val):
    head = None
    node = None
    loop_node = None
    for n in nums:
        if head is None:
            head = ListNode(n)
            node = head
        else:
            new_node = ListNode(n)
            node.next = new_node
            if n == loop_val:
                loop_node = new_node
            node = new_node
    if node is not None:
        node.next = loop_node
    return head


MAX_VALUE = 300
a = Solution()
print(a.detectCycle(convertToList([5, 23, 110, 134], 5)))
print(a.detectCycle(convertToList([27, 42, 81, 116, 124, 130, 169, 228, 298], 130)))
print(a.detectCycle(convertToList([51, 85, 123, 150, 196, 217, 226, 228, 246], 123)))
for _ in range(100):
    size = random.randint(0, 13)
    if size == 0:
        a_list = []
    else:
        a_list = sorted([random.randint(0, MAX_VALUE) for _ in range(size)])
    loop_value = random.randint(0, MAX_VALUE)
    head = convertToList(a_list, loop_value)
    if a.detectCycle(head) != (loop_value if loop_value in a_list else None):
        print("Wrong", a_list, loop_value, a.detectCycle(head))

print("FINISHED")
