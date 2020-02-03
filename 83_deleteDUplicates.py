from testList import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                cur.next =cur.next.next
            else:
                cur = cur.next
        return head



testSolution = Solution()
mhead = getList([1, 1, 2, 3, 3])
printList(mhead)
mhead = testSolution.deleteDuplicates(mhead)
printList(mhead)

