class Solution:
    # dp，不保存子串信息的话，时间会超时
    # def maxVowels(self, s: str, k: int) -> int:
    #     dp_result = [0] * (len(s) + 1)
    #     for i in range (1, len(s) + 1):
    #         dp_result[i] = max(dp_result[i-1],self.countVowels(s[i-k+1:i+1]))
    #     return dp_result
    #
    # def countVowels(self, sub_str):
    #     count = 0
    #     for letter in sub_str:
    #         if letter in ('a', 'e', 'i', 'o','u'):
    #             count += 1
    #     return count

    def maxVowels(self, s: str, k: int) -> int:
        start = 1
        end = k
        max_count = 0
        cur_cnt = 0
        for letter in s[0:k]:
            if letter in ('a', 'e', 'i', 'o','u'):
                cur_cnt += 1
        print(s[0:k])
        print("start_cnt" + ":" + str(cur_cnt))
        while end != len(s):
            if s[start-1] in ('a', 'e', 'i', 'o','u'):
                cur_cnt -= 1
            if s[end] in ('a', 'e', 'i', 'o', 'u'):
                cur_cnt += 1
            print(s[start:end+1])
            print(cur_cnt)
            max_count = max(max_count, cur_cnt)
            start += 1
            end += 1
        return max_count
test_solution = Solution()
print(test_solution.maxVowels("leetcode", 3))



