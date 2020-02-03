from testList import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        tempNext = head.next
        head.next = self.swapPairs(tempNext.next)
        tempNext.next = head
        return tempNext




test = Solution()
testHead = getList([1, 2, 3, 4])
printList(testHead)
testHead = test.swapPairs(testHead)
printList(testHead)
