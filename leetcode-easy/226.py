class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
