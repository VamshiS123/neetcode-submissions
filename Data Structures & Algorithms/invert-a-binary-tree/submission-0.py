# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invertRoot(root):

            if root is None:
                return 0
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            invertRoot(root.left)
            invertRoot(root.right)
        

        invertRoot(root)
        return root



        