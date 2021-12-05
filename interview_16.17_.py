class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_result = [0] * (len(nums) + 1)
        max_value = None
        for index, single_num in enumerate(nums):
            # print("在index为{act_index}的时候，前一部分最大和为{pre_value},当前数组数据为{cur_num}".format(act_index=index, pre_value=dp_result[index], cur_num=single_num), end="\t")
            dp_result[index + 1] = max(dp_result[index] + single_num, single_num)
            # print("在此依据下算出来的最大数据: {max_cur}".format(max_cur=dp_result[index+1]))
            max_value = dp_result[index+1] if max_value is None else max(max_value, dp_result[index+1])
        return max_value
test_solution = Solution()
print(test_solution.maxSubArray([-1,-2,3,4,5,-6,-100,7,8,9]))
