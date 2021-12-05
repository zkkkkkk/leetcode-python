class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getList(valList) -> ListNode:
    head = ListNode(valList[0])
    cur = head
    for i in valList[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


def reverseList(head) -> ListNode:
    pre = None
    cur = head
    while cur is not None:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


def printList(head: ListNode) -> None:
    while head is not None:
        if head.next is not None:
            print(head.val, end='->')
        else:
            print(head.val)
        head = head.next



