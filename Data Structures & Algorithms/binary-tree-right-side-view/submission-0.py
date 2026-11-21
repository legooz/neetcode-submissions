# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        right_side = []
        levels = []
        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()

                levels.append(curr.val)


                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            right_side.append(levels[len(levels) - 1])

            level += 1
        return right_side
            