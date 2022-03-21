"""
@Author: Lzy
@Time: 2022/03/16
@Description: 分治问题
"""

from DivideConquerAlgorithm import TreeNode
from typing import List


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return
    root = TreeNode(preorder[0])
    left_tree_size = inorder.index(root.val)    # 考虑使用dict保存, 获取可以减小时间
    # right_tree_size = len(inorder) - left_tree_size - 1
    root.left = build_tree(preorder[1:left_tree_size+1], inorder[:left_tree_size])
    root.right = build_tree(preorder[left_tree_size+1:], inorder[left_tree_size+1:])
    return root


def my_pow(x: float, n: int) -> float:
    """
    Offer 16. 数值的整数次方
    """
    if x == 0:
        return 0
    res, flag = 1, True
    if n < 0:
        flag = False
        n = -n
    while n:
        if n & 1:
            res *= x
        n = n >> 1
        x = x * x
    return res if flag else 1/res


def verify_post_order(postorder: List[int]) -> bool:
    """
    Offer 33. 二叉搜索树的后序遍历
    """
    stack, root = [], float('+inf')
    for i in range(len(postorder) - 1, -1, -1):
        if postorder[i] > root:
            return False
        while stack and postorder[i] < stack[-1]:
            root = stack.pop()
        stack.append(postorder[i])
    return True


if __name__ == "__main__":
    print(my_pow(2, 10))
