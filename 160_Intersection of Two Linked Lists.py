# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        return p1


def genList(data):
    if not data:
        return None
    head = ListNode(data[0])
    p = head
    for index, value in enumerate(data):
        if index == 0:
            continue
        tempNode = ListNode(value)
        p.next = tempNode
        p = p.next
    return head


def printLinkedList(head):
    while head is not None:
        print(head.val, end='\t')
        head = head.next
    print()


testList = genList([4, 1, 8, 4, 5])
test2List = genList([5, 0, 1])
interNode = testList.next.next
test2List.next.next.next = interNode
printLinkedList(testList)
printLinkedList(test2List)
testCase = Solution()
print(testCase.getIntersectionNode(testList, test2List).val)
