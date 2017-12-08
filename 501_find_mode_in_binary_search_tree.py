# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic={}
        def visit(node):
            if node:
                dic[node.val] = 1 if not dic.has_key(node.val) else dic[node.val] +1
                visit(node.left)
                visit(node.right)
        visit(root)
        dic_sorted = sorted([(k,v) for k,v in dic.iteritems()], key=lambda k: k[1], reverse=True)
        ans_list = []
        for i in range(len(dic_sorted)):
            if dic_sorted[i][1] == dic_sorted[0][1]:
                ans_list.append(dic_sorted[i][0])
            else:
                break
        return ans_list
    
            
