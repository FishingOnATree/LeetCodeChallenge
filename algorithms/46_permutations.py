# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        candidates = set(nums)
        consumed_set = set()
        return self.get_permute(candidates, consumed_set)

    def get_permute(self, candidates, consumed_set):
        if len(candidates) == len(consumed_set):
            return []
        else:
            permutation_list = []
            for candidate in candidates:
                if candidate not in consumed_set:
                    consumed_set_new = set(consumed_set)
                    consumed_set_new.add(candidate)
                    p_list = self.get_permute(candidates, consumed_set_new)
                    if len(p_list):
                        for item in p_list:
                            item.insert(0, candidate)
                            permutation_list.append(item)
                    else:
                        permutation_list.append([candidate])
            return permutation_list

a = Solution()
print(a.permute([1, 2, 3, 4]))