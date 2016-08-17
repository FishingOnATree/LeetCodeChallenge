class Solution(object):
    def containsDuplicate(self, nums):
        my_set = set()
        for n in nums:
            if n in my_set:
                return True
            else:
                my_set.add(n)
        return False

