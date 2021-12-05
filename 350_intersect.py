class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_cnt_dict = {}
        result = []
        for to_store in nums1:
            num_cnt_dict[to_store] = num_cnt_dict.get(to_store, 0) + 1
        for to_query in nums2:
            if num_cnt_dict.get(to_query, 0) > 0:
                result.append(to_query)
                num_cnt_dict[to_query] = num_cnt_dict.get(to_query) - 1
        return result

test_solution = Solution()
print(test_solution.intersect([4,9,5],[9,4,9,8,4]))
