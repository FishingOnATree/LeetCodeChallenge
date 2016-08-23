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


class Solution(object):
    def oddEvenList(self, head):
        if head is not None:
            node = head
            node2 = None
            node2_head = None
            tail = None
            while node is not None and node.next is not None:
                if node2 is None:
                    node2 = node.next
                    node2_head = node2
                else:
                    node2.next = node.next
                    node2 = node2.next
                node.next = node.next.next
                tail = node
                node = node.next
                node2.next = None
            if node is None:
                node = tail
            node.next = node2_head
        return head


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


MAX_VALUE = 300
a = Solution()
print([234, 51, 135, 108, 42, 79, 283, 150, 6, 271, 226, 293, 28, 25, 19, 94, 197, 159, 152, 291])
print(a.oddEvenList(convertToList([234, 51, 135, 108, 42, 79, 283, 150, 6, 271, 226, 293, 28, 25, 19, 94, 197, 159, 152, 291])).print_node())
for _ in range(75):
    size = random.randint(0, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [random.randint(0, MAX_VALUE) for _ in range(size)]
        head = convertToList(a_list)
    print(a_list)
    #print("Original: ", head.print_node())
    #print("Updated:", a.oddEvenList(head).print_node())
