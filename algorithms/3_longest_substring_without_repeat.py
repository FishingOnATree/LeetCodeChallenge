# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        the_set = set()
        the_list = []
        best_list = []
        for char in s:
            if char in the_set:
                if len(best_list) < len(the_list):
                    best_list = list(the_list)
                char_index = the_list.index(char)
                if char_index + 1 < len(the_list):
                    the_list = the_list[(char_index+1):]
                else:
                    the_list = list()
                # reconstruct the set from the list above
                the_set = set([l for l in the_list])
            the_list.append(char)
            the_set.add(char)
        if len(best_list) < len(the_list):
            best_list = list(the_list)
        return len(best_list)


a = Solution()

print(a.lengthOfLongestSubstring("wobgrovw"))
# print(a.lengthOfLongestSubstring("abcdateswdz"))
# print(a.lengthOfLongestSubstring("dvdfe"))
# print(a.lengthOfLongestSubstring(""))
# print(a.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz"))
# print(a.lengthOfLongestSubstring("abaabababababababababababab"))
# print(a.lengthOfLongestSubstring("abcabcbb"))
# print(a.lengthOfLongestSubstring("pwwkew"))
# print(a.lengthOfLongestSubstring("bbbbbb"))

