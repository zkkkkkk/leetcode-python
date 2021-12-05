from testList import *
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        length = 0
        while k != 0:
            k -= 1
            length += 1
            if fast.next is not None:
                fast = fast.next
            else:
                k = k % length
                if k == 0:
                    return head
                fast = head

        # print(slow.val)
        # print(fast.val)
        # if slow == fast:
        #     return head
        print(slow.val,fast.val)
        while slow.next is  not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
        print(slow.val,fast.val)
        fast.next = head
        head = slow.next
        slow.next = None
        return head


# Solution().rotateRight()
testHead = getList([0,1,2])
printList(testHead)
printList(Solution().rotateRight(testHead, 3000000000000000000000000000000000000000000000))
