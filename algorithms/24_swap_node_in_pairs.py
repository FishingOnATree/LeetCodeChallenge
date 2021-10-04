# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            pivot = head
            pivot_next = head.next
            new_head = head.next if head.next else head
            prev = None
            while pivot and pivot_next:
                if prev:
                    prev.next = pivot_next
                pivot.next = pivot_next.next
                pivot_next.next = pivot
                prev = pivot # prev is the 2nd of the swapped node
                pivot = pivot.next
                pivot_next = pivot.next if pivot else None
            return new_head
        else:
            return head

    def print_list(self, head):
        my_list = []
        if head:
            pivot = head
            while pivot:
                my_list.append(pivot.val)
                pivot = pivot.next
        print("result: {}".format(my_list))

    def convert_list(self, a_list):
        if a_list:
            head = None
            prev = None
            for a in a_list:
                node = ListNode(val=a)
                if head == None:
                    head = node
                if prev != None:
                    prev.next = node
                prev = node
            return head
        else:
            return None

for num in range(0, 10, 1):
    a = [i for i in range(0, num)]
    solution = Solution()
    node = solution.convert_list(a)
    print("list: ", a)
    solution.print_list(solution.swapPairs(node))