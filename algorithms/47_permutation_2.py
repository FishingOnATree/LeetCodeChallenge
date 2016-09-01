# https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        return self.get_permute(sorted(nums))

    def get_permute(self, candidates):
        if len(candidates):
            permutation_list = list()
            for index, candidate in enumerate(candidates):
                #print(candidate, (-1 if index == 0 else candidates[index-1]))
                if index == 0 or candidate != candidates[index-1]:
                    candidate_new = list(candidates)
                    candidate_new.pop(index)
                    p_set = self.get_permute(candidate_new)
                    if len(p_set):
                        for item in p_set:
                            item.insert(0, candidate)
                            permutation_list.append(item)
                    else:
                        permutation_list.append([candidate])
            return permutation_list
        else:
            return []

    def permuteUnique2(self, nums):
        p_set = self.get_permute2(nums)
        p_list = []
        for item in p_set:
            p_list.append([int(x) for x in item.split(",")])
        return p_list

    def get_permute2(self, candidates):
        if len(candidates):
            permutation_set = set()
            for index, candidate in enumerate(candidates):
                    candidate_new = list(candidates)
                    candidate_new.pop(index)
                    p_set = self.get_permute(candidate_new)
                    if len(p_set):
                        for item in p_set:
                            permutation_set.add(str(candidate) + "," + item)
                    else:
                        permutation_set.add(str(candidate))
            return permutation_set
        else:
            return []

a = Solution()
print(a.permuteUnique([1, 2, 1]))
print(a.permuteUnique([1, 2, 1, 1]))
# print(a.permuteUnique([2,0,0,1,1,3,3]))