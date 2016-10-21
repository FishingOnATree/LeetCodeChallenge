# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return ", ".join(self.in_order_travese(self))

    def in_order_travese(self, node):
        val_list = []
        if node.left is not None:
            val_list.extend(self.in_order_travese(node.left))
        val_list.append(str(node.val))
        if node.right is not None:
            val_list.extend(self.in_order_travese(node.right))
        return val_list


class Solution(object):
    def sortedListToBST(self, head):
        if head is None:
            return None
        else:
            node = head
            node_list = []
            while node is not None:
                node_list.append(node)
                node = node.next
            return self.build_bst(node_list)

    def build_bst(self, node_list):
        n = len(node_list)
        if n == 1:
            return TreeNode(node_list[0].val)
        else:
            mid = n/2
            root_node = TreeNode(node_list[mid].val)
            if mid > 0:
                root_node.left = self.build_bst(node_list[0:mid])
            if mid < n-1:
                root_node.right = self.build_bst(node_list[(mid+1):])
            return root_node


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
print(a.sortedListToBST(node))
for _ in range(10):
    size = random.randint(1, 25)
    if size == 0:
        a_list = []
    else:
        a_list = [_ for _ in range(size)]
        a_list.sort()
    print(a_list)
