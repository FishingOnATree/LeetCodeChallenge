# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# this is indeed a nxm matrix with the next smallest sum next to one of the previously selected coordinate

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
            tracking_set = set()
            return_list.append([nums1[0], nums2[0]])
            tracking_set.add(tuple((0, 0)))
            while len(return_list) < pivot:
                min_total = nums1[-1] + nums2[-1]
                min_list = [ [len(nums1)-1, len(nums2)-1]]
                #TODO need to find edge
                for u, v in tracking_set:
                    # 3 steps 1 to right, 1 to down or 1 right and 1 down
                    if u+1 < len(nums1):
                        min_total, min_list = self.check_min(tracking_set, min_total, min_list, nums1, nums2, u+1, v)
                    if v+1 < len(nums2):
                        min_total, min_list = self.check_min(tracking_set, min_total, min_list, nums1, nums2, u, v+1)
                    if u+1 < len(nums1) and v+1 < len(nums2):
                        min_total, min_list = self.check_min(tracking_set, min_total, min_list, nums1, nums2, u+1, v+1)
                min_list.sort(key=lambda x: x[0])
                for u, v in min_list:
                    if tuple((u, v)) not in tracking_set:
                        return_list.append([nums1[u], nums2[v]])
                        tracking_set.add(tuple((u, v)))
            return_list = return_list[0:pivot]
        return return_list

    def check_min(self, tracking_set, min_sum, min_list, nums1, nums2, u, v):
        method_min = min_sum
        if tuple((u, v)) not in tracking_set:
            total = nums1[u] + nums2[v]
            if total < min_sum:
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


