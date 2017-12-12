# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        prev = head
        h2 = None
        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
                if not h2:
                    h2 = node
            node = node.next
        return h2
