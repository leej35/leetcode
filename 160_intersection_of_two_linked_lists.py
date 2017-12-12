class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # key idea: make the pre-length same (until the merge point)
        # and compare one by one        
        nodeA, nodeB = headA, headB
        lenA, lenB = 0,0
        
        # get lengths
        while nodeA:
            nodeA = nodeA.next
            lenA += 1
        while nodeB:
            nodeB = nodeB.next
            lenB += 1
        
        # make start point the same
        nodeA, nodeB = headA, headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                nodeA = nodeA.next
        elif lenA < lenB:
            for i in range(lenB-lenA):
                nodeB = nodeB.next
                
        # compare one by one
        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next        
        return nodeA
