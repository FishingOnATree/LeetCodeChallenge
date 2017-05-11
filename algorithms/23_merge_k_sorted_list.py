# https://leetcode.com/problems/merge-k-sorted-lists/#/description
#Definition for singly-linked list.
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-100)
        curr = head
        while True:
            ind = -1
            min_ = None
            rm_list = list()
            for i, node in enumerate(lists):
                if node is None:
                    rm_list.append(i)
                elif min_ is None or node.val < min_:
                    ind = i
                    min_ = node.val
            if ind > -1:
                curr.next = lists[ind]
                curr = curr.next
                lists[ind] = lists[ind].next
            else:
                break
            for index in reversed(rm_list):
                del(lists[index])
        return head.next


import random
a = Solution()
for _ in range(10):
    k = random.randint(1, 10)
    k_list = [sorted([random.randint(0, 100) for _ in range(random.randint(0, 7))]) for _ in range(k)]
    print(k_list)
    k_node_list = list()
    for alist in k_list:
        if alist:
            head = ListNode(-1)
            curr = head
            for val in alist:
                curr.next = ListNode(val)
                curr = curr.next
            k_node_list.append(head.next)
    blist = list()
    for item in k_list:
        blist += item

#    print(a.mergeKLists(k_node_list).get_values())
#     print("--------")
#     print(sorted(blist))
    assert (a.mergeKLists(k_node_list).get_values() == sorted(blist))