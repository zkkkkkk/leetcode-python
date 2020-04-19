from testList import *


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        N = 0
        while  cur:
            cur = cur.next
            N += 1
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur: cur = cur.next
            ans.append(head.next)
        return ans


# test = Solution()
# source = getList([1,2,3,4])
# result = test.splitListToParts(source, 5)

