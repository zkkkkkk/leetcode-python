class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # main_index= 0
        # sub_index= 0
        # while main_index < len(t) and sub_index < len(s):
        #     # print("parent letter:{}, sub letter:{}".format())
        #     if t[main_index] == s[sub_index]:
        #         sub_index+=1
        #     main_index += 1
        # return sub_index == len(s)
        """
        动态规划解法
        """
        t_len = len(t)
        s_len = len(s)
        dp = [[t_len]*26 for _ in range(t_len+1)]
        for i in range(t_len-1, -1, -1):
            print(t[i])
            for j in range(26):
                # print("this i={}, j={}".format(i, j ))
                if ord(t[i]) - ord('a') == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i+1][j]
        print(dp)
        position = 0
        for letter in s:
            print("letter = {}, position = {}".format(letter, position))
            if dp[position][ord(letter)-ord('a')] == t_len:
                return False
            position = dp[position][ord(letter) - ord('a')]+1
        return True


test_instance = Solution()
print(test_instance.isSubsequence("aaaaaa", "bbaaaa"))