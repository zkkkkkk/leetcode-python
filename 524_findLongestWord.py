class Solution(object):
     def  isSubString(self, s, t):
         i = 0
         j = 0
         while (i < len(s) and j < len(t)):
            if s[i] == t[j]:
                j += 1
            i += 1
         return j == len(t)

     def findLongestWord(self, s, d):
        longestWord = ""
        for keyWord in d:
            if len(keyWord) > len(longestWord) or longestWord > keyWord and len(longestWord) == len(keyWord):
                if self.isSubString(s, keyWord):
                    longestWord = keyWord
        return longestWord
test = Solution()
print(test.findLongestWord("aaa", ["aaa","a","a"]))
