class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head.next
        slow = head
        while (slow is not None and fast is not None and fast.next is not None):
            if (slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next
        return False


