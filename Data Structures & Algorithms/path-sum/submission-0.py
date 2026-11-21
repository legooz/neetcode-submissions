# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0

        def leafPath(root, pathSum):
                if not root:
                    return False
                print(pathSum)
                pathSum += root.val

                if pathSum == targetSum and not root.left and not root.right:
                    return True
                if leafPath(root.left, pathSum):
                    return True
                if leafPath(root.right, pathSum):
                    return True

                return False
        return leafPath(root, pathSum)


