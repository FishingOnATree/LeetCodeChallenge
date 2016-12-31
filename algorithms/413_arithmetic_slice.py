import random

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        else:
            start = 0
            diff = A[1] - A[0]
            slice_list = list()
            for index in range(2, len(A)):
                if diff != (A[index] - A[index-1]):
                    # end of a slice
                    slice_len = index - start
                    if slice_len >= 3:
                        # print(index, start)
                        slice_list.append(slice_len)
                    diff = A[index] - A[index-1]
                    start = index - 1
            if len(A) - start >= 3:
                slice_list.append(len(A) - start)
            total = 0
            for list_len in slice_list:
                for length in range(3, list_len):
                    total += list_len - length + 1
                total += 1
            # print(slice_list)
            # print(total)
            return total

def generateList(n):
    the_list = [0] * n
    diff = random.randint(-100, 100)
    for index in range(1, n):
        if random.random() < 0.4:
            diff = random.randint(-100, 100)
        the_list[index] = the_list[index-1] + diff
    return the_list

a = Solution()
a.numberOfArithmeticSlices([4, 4, 6, 4, 4, 4, 4, 4, 4, 4, 3, 2, 3, 4])
for _ in range(100):
    print(generateList(random.randint(1, 100)))
