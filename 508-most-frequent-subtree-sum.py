# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        self.h={}
        self.visit(root)
        
        l = [(k,v) for k,v in self.h.iteritems()]
        l = sorted(l, key=lambda x:x[1], reverse=True)
        maxv = l[0][1]
        
        return [k for (k,v) in l if v == maxv]
        
        
    def visit(self, node):
        if node:
            v = node.val
            v += self.visit(node.left)
            v += self.visit(node.right)

            if self.h.has_key(v):
                self.h[v]+=1
            else:
                self.h[v] =1

            return v
        else:
            return 0
