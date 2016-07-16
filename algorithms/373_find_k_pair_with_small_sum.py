# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# this is indeed a nxm matrix with the next smallest sum next to one of the previously selected coordinate
import timeit

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        return_list = []
        if nums1 and nums2 and k > 0:
            # slice nums1 and nums2
            if len(nums1) > k: nums1 = nums1[0:k]
            if len(nums2) > k: nums2 = nums2[0:k]
            row_count = len(nums1)
            col_count = len(nums2)
            return_size = min(k, row_count * col_count)
            edge_col_position = [[0, n+nums2[0]] for n in nums1]
            tracking_set = set()
            max_value = nums1[-1] + nums2[-1] + 1
            while len(return_list) < return_size:
                min_value = max_value
                min_list = None
                for row_index, col in enumerate(edge_col_position):
                    col_index, cell_value = col
                    if tuple((row_index, col_index)) not in tracking_set:
                        if cell_value < min_value:
                            min_value = cell_value
                            min_list = [[row_index, col_index]]
                        elif cell_value == min_value:
                            min_list.append([row_index, col_index])
                for row, col in min_list:
                    tracking_set.add(tuple((row, col)))
                    return_list.append([nums1[row], nums2[col]])
                    if col+1 < col_count:
                        edge_col_position[row] = [col+1, nums1[row] + nums2[col+1]]
            return_list = return_list[0:return_size]
        return return_list


a = Solution()
t0 = timeit.default_timer()
for _ in range(100):
    print("[1, 7, 11], [2, 4, 6], 3 =>", a.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
    print("[1, 1, 2], [1, 2, 3], 10 =>", a.kSmallestPairs([1, 1, 2], [1, 2, 3], 10))
    print("[1, 1, 2], [1, 2, 3], 2 =>", a.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
    print("[1, 2], [3], 3 =>", a.kSmallestPairs([1, 2], [3], 3))
    print("[1, 2, 3, 5, 10], [3, 3, 4, 5, 6], 5 =>", a.kSmallestPairs([1, 2, 3, 5, 10], [3, 3, 4, 5, 6], 5))
    print("[1, 100], [1, 2, 3, 3, 4, 5, 6], 5 =>", a.kSmallestPairs([1, 100], [1, 2, 3, 3, 4, 5, 6], 5))
print("Total time: % .6f" % (timeit.default_timer() - t0))

