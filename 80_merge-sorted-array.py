class Solution:
    def merge(self, nums1, m, nums2, n):
        index = m + n -1
        while index != 0 and m!=0 and  n != 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[index] = nums2[n-1]
                n -= 1
            else:
                nums1[index] = nums1[m-1]
                m -= 1
            index -= 1
        if n != 0:
            while n != 0:
                nums1[index] = nums2[n-1]
                index-=1
                n-=1

        return nums1

test = Solution()
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
print(test.merge(nums1,nums1.index(0), nums2, len(nums2)))





