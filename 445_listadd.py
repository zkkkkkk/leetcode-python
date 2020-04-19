from testList import *
import  math


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # rhead1 = reverseList(l1)
        # rhead2 = reverseList(l2)
        # result = rhead1
        # pre1 = None
        # pre2 = None
        # addnum = 0
        # while rhead1 is not None and rhead2 is not None:
        #     tempVal = (rhead1.val + rhead2.val) % 10 + addnum
        #     addnum = math.floor((rhead1.val + rhead2.val)/10)
        #     rhead1.val = tempVal
        #     pre1 = rhead1
        #     pre2 = rhead2
        #     rhead1 = rhead1.next
        #     rhead2 = rhead2.next
        #     print(addnum)
        # if rhead1 is None:
        #     pre1.next = rhead2
        #
        # if addnum != 0:
        #     while pre1.next is not None:
        #         pre1 = pre1.next
        #     pre1.next = ListNode(addnum)
        # return reverseList(result)
        stackA = []
        stackB = []
        while l1 is not None:
            stackA.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stackB.append(l2.val)
            l2 = l2.next
        res = []
        addNum = 0
        while stackA and stackB :
            tempVal = stackA.pop() + stackB.pop() + addNum
            res.append(tempVal % 10)
            addNum = math.floor(tempVal/10):wq：：::::
        while stackA::q::
            tempVal = stackA.pop() + addNum
            res.append(tempVal%10)
            addNum = math.floor(tempVal/10)
        while stackB:
            tempVal = stackB.pop() + addNum
            res.append(tempVal%10)
            addNum = math.floor(tempVal/10)
        if addNum:
            res.append(addNum)
        newHead = ListNode(res.pop())
        cur = newHead
        while res:
            cur.next = ListNode(res.pop())
            cur = cur.next
        return newHead



test = Solution()
h1 = getList([1])
h2 = getList([9,9])
printList(h1)
printList(h2)
printList(test.addTwoNumbers(h1, h2))
