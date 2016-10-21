# https://leetcode.com/problems/edit-distance/
import random

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        self.distance_matrix = []
        self.distance_matrix.append([i for i in range(0, n+1)])
        for j in range(1, m+1):
            space = [j]
            space.extend([-1] * n)
            self.distance_matrix.append(space)
        min_value = self.find_min_distance(word1, n, word2, m, max(n, m))
        return min_value

    def find_min_distance(self, w1, i, w2, j, max_dist):
        if self.distance_matrix[j][i] >= 0:
            return self.distance_matrix[j][i]
        else:
            if w1[i-1] == w2[j-1]:
                # replace same cost as ins/del, it guarantees minimal edit distance
                min_value = self.find_min_distance(w1, i-1, w2, j-1, max_dist) if i > 0 and j > 0 else max_dist
            else:
                min_dist_del = (self.find_min_distance(w1, i-1, w2, j, max_dist) if i > 0 else max_dist) + 1
                min_dist_ins = (self.find_min_distance(w1, i, w2, j-1, max_dist) if j > 0 else max_dist) + 1
                min_dis_rep = 1 + (self.find_min_distance(w1, i-1, w2, j-1, max_dist) if i > 0 and j > 0 else max_dist)
                min_value = min(min_dist_del, min_dist_ins, min_dis_rep)
            self.distance_matrix[j][i] = min_value
            return min_value

    def pretty_print(self, mat):
        for m in mat:
            print(m)

a = Solution()
print(a.minDistance("", "bcd"))
print(a.minDistance("abc", "bcd"))
print(a.minDistance("apples", "pears"))
for _ in range(0):
    length = 3 + random.randint(0, 30)
    string1 = [chr(random.randint(0, 25) + (ord('a') if random.random() <= 0.5 else ord('A'))) for _ in range(length)]
    print('"' + "".join(string1) + '"')