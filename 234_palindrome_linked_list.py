# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # count number of nodes
        c=0
        node = head        
        while node:
            node = node.next
            c+=1
        
        # reverse first half
        node = head
        prev = None
        for i in range(c//2):
            _n_next = node.next
            node.next = prev
            prev = node
            node = _n_next
        
        h1 = prev
        
        # pointer to the second half
        if c%2 == 0:
            h2 = node
        else:
            h2 = node.next
        
        # compare second half and reversed first half
        while h1:
            if h1.val ==  h2.val:
                h1 = h1.next
                h2 = h2.next
            else:
                return False
        return True
