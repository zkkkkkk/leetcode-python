class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if l1 is None:
    #         return l2
    #     if l2 is None:
    #         return l1
    #     if l1.val <= l2.val:
    #         head = l1
    #         l1 = l1.next
    #     else:
    #         head = l2
    #         l2 = l2.next
    #     while l1 is not None and l2 is not None:
    #         if l1.val <= l2.val:
    #             head.next = l1
    #             l1 = l1.next
    #         else:
    #             head.next = l2
    #             l2 = l2.next
    #         head = head.next
    #     if l1 is not None:
    #         head.next = l1
    #     else:
    #         head.next = l2
    #     return head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeRecurisive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeRecurisive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeRecurisive(l2.next, l1)
            return l2


