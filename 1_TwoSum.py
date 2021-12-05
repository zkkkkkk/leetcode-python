class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        code_dict = {}
        for index, single_value in enumerate(nums):
            if code_dict.__contains__(single_value):
                return [code_dict.get(single_value), index]
            code_dict[target -single_value] = index
        return []

test_object = Solution()
print(test_object.twoSum([2, 7, 11, 15], 27))