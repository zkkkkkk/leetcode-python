class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverseHelper(len(s) - 1, s)

    def reverseHelper(self, index, s):
        s_length = len(s)
        mid_index = s_length / 2
        if index < mid_index:
            return
        temp_char = s[index]
        s[index] = s[s_length - index - 1]
        s[s_length - index - 1] = temp_char
        self.reverseHelper(index - 1, s)
        return


testSolution = Solution()
testString = ['a','b','c','d']
testSolution.reverseString(testString)
print(testString)
