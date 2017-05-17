# https://leetcode.com/problems/generate-parentheses/#/description

class Solution(object):
    def generateParenthesis(self, n):
        return_list = list()
        if n < 0:
            return [""]
        self.genParenthesis(0, 0, n, "", return_list)
        return return_list

    def genParenthesis(self, on, cn, n, curr_string, my_list):
        if on == cn == n:
            my_list.append(curr_string)
        else:
            if on < n:
                self.genParenthesis(on + 1, cn, n, curr_string + "(", my_list)
            if on > cn and cn < n:
                self.genParenthesis(on, cn + 1, n, curr_string + ")", my_list)

a = Solution()
print(a.generateParenthesis(3))