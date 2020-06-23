import sys


class Solution:
    def longestCommonPrefix(self, strs):
        # 暴力解，o(n)
        # 可以分治拓展。首先每两个字符串之间找最大公共部分，迭代得到全局结果。这个过程可以分治并发执行
        result_str = ""
        if not strs:
            return result_str
        for index_i in range(0, sys.maxsize):
            this_char = ""
            for single_str in strs:
                if index_i == len(single_str) or this_char != "" and this_char != single_str[index_i]:
                    return result_str
                this_char = single_str[index_i]
            result_str += this_char


test_object = Solution()
print(test_object.longestCommonPrefix([]))
