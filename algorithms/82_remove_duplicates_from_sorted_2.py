
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
    def deleteDuplicates(self, head):
        if head is None:
            return None
        else:
            return_node = None
            return_node_tail = None
            node = head
            while node is not None:
                if node.next is not None and node.next.val == node.val:
                    while node.next is not None and node.next.val == node.val:
                        node = node.next
                    node = node.next
                else:
                    this_node = node
                    node = node.next
                    if return_node is None:
                        return_node = this_node
                        return_node_tail = this_node
                    else:
                        return_node_tail.next = this_node
                        return_node_tail = this_node
                    this_node.next = None
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
a.deleteDuplicates(convertToList([1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8])).print_node()
for _ in range(100):
    size = random.randint(0, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [random.randint(0, MAX_VALUE) for _ in range(size)]
        a_list.sort()
        head = convertToList(a_list)
    print(a_list)
    #print("Original: ", head.print_node())
    #print("Updated:", a.oddEvenList(head).print_node())