class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        ListNode
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    # def reverseList(self, head: ListNode) -> ListNode:
    #     pre = None
    #     while head is not None:
    #         temp = head.next
    #         head.next = pre
    #         pre = head
    #         head = temp
    #     return head


