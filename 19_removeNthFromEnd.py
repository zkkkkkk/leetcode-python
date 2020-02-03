from testList import *
class Solution:
    def removeNthFromEnd(self, head: ListNode, n:int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while n != -1:
            fast = fast.next
            n -= 1
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


test = Solution()
testHead = getList([1])
testHead = test.removeNthFromEnd(testHead, 1)
printList(testHead)
