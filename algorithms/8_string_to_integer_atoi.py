class Solution:
    def myAtoi(self, string: str) -> int:
        capture = list()
        start_idx = -1
        target = string.lstrip()
        if len(target):
            product = 1
            if target[0] == '-':
                product = -1
                target = target[1:]
            elif target[0] == '+':
                target = target[1:]

            num_str = list()
            for c in target:
                if c.isdigit():
                    num_str.append(c)
                else:
                    break
            if num_str:
                if product == 1:
                    return min(pow(2, 31) -1, int(''.join((num_str))))
                else:
                    return max(pow(2, 31) * -1, -1 * int(''.join((num_str))))
        return 0


print(Solution().myAtoi("-"))
print(Solution().myAtoi("+"))
print(Solution().myAtoi("+ 121"))