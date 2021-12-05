class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.cal_range(nums, 1, n-1), self.cal_range(nums, 0, n-2))

    def cal_range(self, nums, start, end):
        print("start:{}, end:{}".format(start, end))
        pre1 = 0
        pre2 = 0
        cur = 0
        for i in range(start, end+1):
            print("cur stat, pre2:{}, pre1:{}, cur{}".format(pre2,pre1,cur))
            cur = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return cur

test_instanct = Solution()
print(test_instanct.rob([1,2,3,1]))