# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from testList import *;


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        cur = head
        cnt = 1
        reverseHead = None
        reverseTail = None
        while cnt <= n:
            print(cnt)
            try:
                print(cur.val)
                print(pre.val)
            except :
                print("not a valid node")
                print("current cnt = " + str(cnt))

            if cnt > m:
                Tempnext = cur.next
                cur.next = pre
                cur = Tempnext
                pre = cur
            elif cnt == n:
                reverseHead.next = cur
                reverseTail.next = cur.next
                cur.next = pre
            else:
                if cnt == m:
                    reverseHead = pre
                    reverseTail = cur
                pre = cur
                cur = cur.next
            cnt += 1
        return reverseHead.next if m == 1 else head









testInstance = Solution()
mylist = getList([1, 2, 3, 4, 5])
printList(mylist)
printList(testInstance.reverseBetween(mylist,2,4))
