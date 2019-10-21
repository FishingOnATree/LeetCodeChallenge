class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        str_list = [list() for _ in range(numRows)]
        counter = 0
        direction = 1
        for c in s:
            str_list[counter].append(c)
            if counter + 1 == numRows and direction == 1:
                direction = -1
            if counter == 0 and direction == -1:
                direction = 1
            counter += direction
        rtn = ""
        for s_list in str_list:
            rtn += "".join(s_list)
        return rtn


Solution().convert()
