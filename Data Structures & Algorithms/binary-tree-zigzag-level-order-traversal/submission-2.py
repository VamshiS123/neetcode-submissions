# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []


        queue = deque([root])
        res = []

        right_to_left = True

        while queue:
            level = []

            for _ in range(len(queue)):

                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


            if not right_to_left:
                level.reverse()
            
            res.append(level)

            right_to_left = not right_to_left


        return res

                
        