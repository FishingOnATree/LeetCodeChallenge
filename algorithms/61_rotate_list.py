# https://leetcode.com/problems/rotate-list/
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
    def rotateRight(self, head, k):
        if head is None:
            return None
        else:
            count = 0
            node = head
            while node is not None:
                node = node.next
                count += 1
            new_tail_no = count - (k % count)
            if new_tail_no == count:
                #no shift necessary
                return head
            else:
                count = 1
                node = head
                while node is not None and new_tail_no != count:
                    node = node.next
                    count += 1
                tail = node
                node = node.next
                new_head = node
                while node.next is not None:
                    node = node.next
                node.next = head
                tail.next = None
                return new_head


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
# a_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a_list, 0)
# a.rotateRight(convertToList(a_list), 0).print_node()
# print(a_list, 1)
# a.rotateRight(convertToList(a_list), 1).print_node()
# print(a_list, 5)
# a.rotateRight(convertToList(a_list), 5).print_node()
# print(a_list, 7)
# a.rotateRight(convertToList(a_list), 7).print_node()
# print(a_list, 8)
# a.rotateRight(convertToList(a_list), 8).print_node()
# print(a_list, 10)
# a.rotateRight(convertToList(a_list), 10).print_node()

for _ in range(100):
    size = random.randint(0, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [random.randint(0, MAX_VALUE) for _ in range(size)]
        head = convertToList(a_list)
    print(a_list)
    print(random.randint(0, 100))
    #print("Original: ", head.print_node())
    #print("Updated:", a.oddEvenList(head).print_node())