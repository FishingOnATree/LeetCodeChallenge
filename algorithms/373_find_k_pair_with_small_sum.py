# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# this is indeed a nxm matrix with the next smallest sum next to one of the previously selected coordinate
import sys

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        return_list = []
        if nums1 and nums2 and k > 0:
            # slice nums1 and nums2
            if len(nums1) > k: nums1 = nums1[0:k]
            if len(nums2) > k: nums2 = nums2[0:k]
            return_size = k if k <= len(nums1) * len(nums2) else len(nums1) * len(nums2)
            tracking_matrix = [[False for _ in nums2] for _ in nums1]
            edge_col_position = [0] * len(nums1)

            #init first item
            return_list.append([nums1[0], nums2[0]])
            tracking_matrix[0][0] = True
            edge_col_position[0] = 0

            while len(return_list) < return_size:
                min_total = sys.maxint
                min_list = []
                for row_index, row in enumerate(tracking_matrix):
                    starting_col = 0 if edge_col_position[row_index] is None else edge_col_position[row_index]
                    for col_index in range(starting_col, len(row)):
                        if not row[col_index]:
                            break
                    edge_col_position[row_index] = col_index
                for row_index, col_index in enumerate(edge_col_position):
                    min_total, min_list = self.check_min(tracking_matrix, min_total, min_list, nums1, nums2, row_index, col_index)
                for u, v in min_list:
                    if not tracking_matrix[u][v]:
                        return_list.append([nums1[u], nums2[v]])
                        tracking_matrix[u][v] = True
                        edge_col_position[u] = v
            return_list = return_list[0:return_size]
        return return_list

    def check_min(self, tracking_matrix, min_sum, min_list, nums1, nums2, u, v):
        method_min = min_sum
        if not tracking_matrix[u][v]:
            total = nums1[u] + nums2[v]
            if total < method_min:
                method_min = total
                min_list = [[u, v]]
            elif total == method_min:
                min_list.append([u, v])
        return method_min, min_list


a = Solution()
print("[1, 7, 11], [2, 4, 6], 3 =>", a.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print("[1, 1, 2], [1, 2, 3], 10 =>", a.kSmallestPairs([1, 1, 2], [1, 2, 3], 10))
print("[1, 1, 2], [1, 2, 3], 2 =>", a.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print("[1, 2], [3], 3 =>", a.kSmallestPairs([1, 2], [3], 3))
print("[1, 2, 3, 5, 10], [3, 3, 4, 5, 6], 5 =>", a.kSmallestPairs([1, 2, 3, 5, 10], [3, 3, 4, 5, 6], 5))
print("[1, 100], [1, 2, 3, 3, 4, 5, 6], 5 =>", a.kSmallestPairs([1, 100], [1, 2, 3, 3, 4, 5, 6], 5))


