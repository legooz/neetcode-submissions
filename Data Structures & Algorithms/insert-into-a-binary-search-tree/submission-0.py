# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # 3rd: (None, 6)
            return TreeNode(val) # return TreeNode(6) to 2nd

        if val > root.val: # 1st: 6 > 5? yes. :: 2nd: 6 > 9? No.
            root.right = self.insertIntoBST(root.right, val) # 1st: root.right = ? insert(9, 6) :: returned 9 from 2nd
        elif val < root.val: # 2nd: 6 < 9? yes.
            root.left = self.insertIntoBST(root.left, val) # 2nd: insert(None, 6) - get returned TreeNode(6)

        return root # returns 9 to the 1st one - returns 5 from the 1st