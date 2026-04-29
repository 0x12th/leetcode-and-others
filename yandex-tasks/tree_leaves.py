"""
Дано бинарное дерево, значения в нем - числа.
Нужно написать функцию, которая возвращает сумму всех узлов дерева, у которых нет потомков.

Пример:

    5
   / \
  4   2
 / \   \
1   6   3
       /
      7

sum = 14 (1 + 6 + 7)
"""


class TreeNode:
    def __init__(
        self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None
    ):
        self.val = val
        self.left = left
        self.right = right


def sum_leaves(root: TreeNode | None) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    return sum_leaves(root.left) + sum_leaves(root.right)
