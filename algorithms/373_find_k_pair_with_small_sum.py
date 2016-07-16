# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        return_list = []
        if nums1 and nums2:
            # slice nums1 and nums2
            if len(nums1) > k:
                nums1 = nums1[0:k]
            if len(nums2) > k:
                nums2 = nums2[0:k]
            possible_combo = len(nums1) * len(nums2)
            pivot = k if k <= possible_combo else possible_combo
            sum_list = [ [[u, n], u+n] for u in nums1 for n in nums2]
            sum_list.sort(key=lambda x: (x[1], x[0][0]))
            return_list = [sum_list[index][0] for index in range(pivot)]
        return return_list


a = Solution()
print("[1, 7, 11], [2, 4, 6], 3 =>", a.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print("[1, 1, 2], [1, 2, 3], 2 =>", a.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print("[1, 2], [3], 3 =>", a.kSmallestPairs([1, 2], [3], 3))
print("[1, 2, 3, 5, 10], [3, 3, 4, 5, 6], 5 =>", a.kSmallestPairs([1, 2, 3, 5, 10], [3, 3, 4, 5, 6], 5))
print("[1, 100], [1, 2, 3, 3, 4, 5, 6], 5 =>", a.kSmallestPairs([1, 100], [1, 2, 3, 3, 4, 5, 6], 5))


