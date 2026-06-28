# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeheight(self,root):
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        
        return 1+max(self.treeheight(root.left),self.treeheight(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        if not root:
            return 0
        
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)

            diameter=max(diameter,left+right)
            return 1+max(left,right)

        dfs(root)
        return diameter        