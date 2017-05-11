# https://leetcode.com/problems/add-and-search-word-data-structure-design/#/description

import collections

class WordDictionary(object):

    def __init__(self):
        self.word_dictionary = collections.defaultdict(list)

    def addWord(self, word):
        self.word_dictionary[len(word)].append(word)

    def search(self, target):
        if target:
            for word in self.word_dictionary[len(target)]:
                i = 0
                for l1, l2 in zip(target, word):
                    if l1 != "." and l1 != l2:
                        break
                    i += 1
                if i == len(target):
                    return True
        return False

a = WordDictionary()
a.addWord("bad")
a.addWord("dad")
a.addWord("mad")
print(a.search("pad"))
print(a.search("bad"))
print(a.search(".ad"))
print(a.search("b.."))
print(a.search("."))
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)