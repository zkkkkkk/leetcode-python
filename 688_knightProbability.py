class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        slow_dp = [[0]*N for _ in range(N)]
        slow_dp[r][c] = 1
        for _ in range(K):
            fast_dp = [[0]*N for _ in range(N)]
            for row_index, row_value in enumerate(slow_dp):
                for column_index, column_value in enumerate(row_value):
                    for x_change, y_change in (2,1),(-2,1),(2,-1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2):
                          if 0<= row_index + x_change <N and 0<=column_index + y_change < N:
                              # print("raw point, ({}, {});delta, ({}, {})".format(row_index, column_index, x_change, y_change))
                              fast_dp[row_index+x_change][column_index+y_change] += column_value/8.0
            slow_dp = fast_dp
        return sum(map(sum,slow_dp))
test_instance = Solution()
