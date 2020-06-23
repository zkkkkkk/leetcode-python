def innerJudge(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def validPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return innerJudge(s, i + 1, j) or innerJudge(s, i, j - 1)
        i += 1
        j -= 1
    return True


class Solution:
    pass


test = Solution()
print(validPalindrome("aba"))
