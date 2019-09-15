class Solution:
    def innerJudge(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def validPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.innerJudge(s,i+1,j) or self.innerJudge(s,i,j-1)
            i += 1
            j -= 1
        return True
test = Solution()
print(test.validPalindrome("aba"))




