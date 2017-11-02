# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
    def get_dict(self, node, level, tree_map):
        
        if node.right:
            self.get_dict(node.right, level+1, tree_map)
        
        if node.left:
            self.get_dict(node.left, level+1, tree_map)
        
        if not self.tree_map.has_key(level):
            tree_map[level] = []
        
        tree_map[level].append(node.val)
    
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.tree_map = {}
        self.get_dict(root, 0, self.tree_map)
        
        return [float(sum(v))/len(v) for v in self.tree_map.values()]
