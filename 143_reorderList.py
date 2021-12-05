# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import testList
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        midNode = self.getMidNode(head)
        rightHead = midNode.next
        midNode.next = None
        return self.mergeList(head, self.reverseList(rightHead))

    def mergeList(self, head1, head2):
        totalHead = head1
        cHead1 = head1
        cHead2 = head2
        while cHead1.next is not None and cHead2 is not None:
            needMoveNode = cHead2
            cHead2 = cHead2.next
            needMoveNode.next = cHead1.next
            cHead1.next = needMoveNode
            cHead1 = needMoveNode.next
        if cHead2 is not None:
            cHead1.next = cHead2
        return totalHead


    def getMidNode(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pre = head
        cur = head.next
        pre.next = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre





test_class = Solution()
test_object = testList.getList([1,2,3,4])
testList.printList(test_class.reorderList(test_object))
