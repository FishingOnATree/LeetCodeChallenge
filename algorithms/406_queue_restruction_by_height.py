import collections

class Solution(object):
    def reconstructQueue(self, people):
        partition = collections.defaultdict(list)
        for height, taller in people:
            partition[height].append(taller)
        for k, v in partition.iteritems():
            partition[k] = sorted(v)
        heights = sorted(partition.keys(), reverse=True)
        return_list = list()
        for height in heights:
            for taller in partition[height]:
                # use a linked list would potentially improve performance.
                return_list.insert(taller, [height, taller])
        return return_list

a = Solution()
print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
