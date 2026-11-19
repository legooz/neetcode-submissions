# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if(root.val < key):
            root.right = self.deleteNode(root.right, key)
        elif(root.val > key): # 1st : 5 > 3 :: root.left = ? :: self.deleteNode(3, 3)
            root.left = self.deleteNode(root.left, key)
        else: # cases where we find the value and there is 0 or 1 child
            if not root.left: 
                return root.right
            elif not root.right:
                return root.left
            else: # case where we find the value and there is 2 children
                miniNode = minNode(root.right)
                root.val = miniNode.val
                root.right = self.deleteNode(root.right, miniNode.val)

        return root
