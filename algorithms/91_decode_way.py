# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

class Solution:

    def numDecodings(self, s: str) -> int:
        sub_strings = self.section_by_zero(s)
        no_way = 1
        for part in sub_strings:
            if part == "0":
                return 0 # short cut condition
        for part in sub_strings:
            no_way *= self.find_ways(part)
            if no_way == 0:
                return no_way
        return no_way

    def find_ways(self, part: str) -> int:
        if len(part) <= 2:
            if part[0] == "0" or (int(part) > 26 and part[1] == "0"):
                return 0
            elif len(part) == 1:
                return 1
            elif len(part) == 2 and (int(part) > 26 or part[1] == "0"):
                return 1
            else:
                return 2
        else:
            result = 0
            result += self.find_ways(part[1:])
            if int(part[0:2]) <= 26:
                result += self.find_ways(part[2:])
            return result

    def section_by_zero(self, s: str) -> list:
        sub_string_list = []
        size = len(s)
        pivot = 0
        try:
            while pivot < size:
                index = s.index("0", pivot, size)
                sub_string_list.append(s[pivot:index+1])
                pivot = index+1
        except ValueError:
            last_part = s[pivot:]
            if last_part:
                sub_string_list.append(last_part)
        return sub_string_list


a = Solution()
ss = ["27", "198", "11810", "1181019", "12", "226", "06", "111111111111111111111111111111111111111111111"]
for s in ss:
    print(s, " --> ", a.section_by_zero(s))
    print(s, " --> ", a.numDecodings(s))