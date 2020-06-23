from testList import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ListArray = []
        ListLength = 0
        while head is not None:
            ListArray.append(head.val)
            head = head.next
            ListLength += 1
        resultFlag = True
        low = 0
        high = ListLength - 1
        while low < high:
            if ListArray[low] != ListArray[high]:
                resultFlag = False
            low += 1
            high -= 1
        return resultFlag


test = Solution()
testList = getList([1, 2, 2, 3,1])
print(test.isPalindrome(testList))
