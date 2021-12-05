class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(2, n+1):
            print("i="+str(i))
            for j in range(1, i):
                print("j="+str(j))
                dp[i] = max(dp[i], j*(i-j), j * dp[i-j])
        return dp[i]
test_instanct = Solution()
print(test_instanct.integerBreak(2))
