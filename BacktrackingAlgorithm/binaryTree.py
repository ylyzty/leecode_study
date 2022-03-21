"""
@Author: Lzy
@Time: 2022/03/07
@Description: 二叉树的回溯问题
"""
from typing import List
from BacktrackingAlgorithm.TreeNode import TreeNode

"""
参数传递, 可更改与不可更改对象
mutable: list, dict, set, 引用传递, 函数内部修改会影响外部参数
immutable: tuple, number, string, 值传递, 函数内部修改不影响本身
"""


def k_th_largest(root: TreeNode, k: int) -> int:
    """中序遍历倒序"""
    res = []
    k_th_largest_dfs(root, res, k)
    return res[-1]


def k_th_largest_dfs(root: TreeNode, res: List[int], k: int) -> List[int]:
    """遍历到第 K 个点结束"""
    if not root:
        return
    k_th_largest_dfs(root.right, res, k)
    if len(res) >= k:
        return res
    res.append(root.val)
    k_th_largest_dfs(root.left, res, k)
    return res


def path_sum(root: TreeNode, target: int) -> List[List[int]]:
    """
    Offer 34. 二叉树中和为某一值二的路径
    """
    res, temp = [], []
    return path_sum_dfs(root, target, res, temp)


def path_sum_dfs(root: TreeNode, target: int, res: List[List[int]], temp: List[int]):
    if not root:
        return

    temp.append(root.val)
    if target == sum(temp) and not root.left and not root.right:
        res.append(temp[:])
    path_sum_dfs(root.left, target, res, temp)
    path_sum_dfs(root.right, target, res, temp)
    temp.pop()


def tree_to_doubly_list(root: TreeNode) -> TreeNode:
    """
    Offer36. 二叉搜索树与双向链表
    核心: 中序遍历
    :param root:
    :return:
    """

    def tree_to_doubly_list_dfs(cur: TreeNode):
        nonlocal pre, head
        if not cur:
            return
        tree_to_doubly_list_dfs(cur.left)
        if pre:
            pre.right, cur.left = cur, pre
        else:
            head = cur
        pre = cur
        tree_to_doubly_list_dfs(cur.right)

    if not root:
        return
    pre, head = None, None
    tree_to_doubly_list_dfs(root)
    head.left, pre.right = pre, head
    return head


def max_depth(root: TreeNode) -> int:
    """
    Offer 55-I. 二叉树的深度
    """
    if not root:
        return 0
    return max(max_depth(root.left), max(root.right)) + 1


def is_balanced(root: TreeNode) -> bool:
    """
    Offer 55-II. 判断是否为平衡二叉树: 二叉树中的任意节点的左右子树的深度相差不超过1
    先序遍历, 产生大量重复计算
    """
    if not root:
        return True
    return abs(max_depth(root.left) - max_depth(root.right)) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def is_balanced_2(root: TreeNode) -> bool:
    """
    后序遍历 + 剪枝
    """

    def recur(root):
        if not root:
            return 0
        left = recur(root.left)
        if left == -1:
            return -1
        right = recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1

    return recur(root) != -1


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Offer 68-I. 二叉搜索树的最近公共祖先
    """
    if root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    return root


def lowest_common_ancestor_2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Offer 68-II. 二叉树的公共结点
    """
    if not root or root.val == p.val or root.val == q.val:
        return root
    left = lowest_common_ancestor_2(root.left, p, q)
    right = lowest_common_ancestor_2(root.right, p, q)
    if not left and not right:
        return None     # 左右子树均不包含p,q
    if not left:
        return right    # 右子树包含p和q
    if not right:
        return left     # 左子树包含p和q
    return root         # p,q分别落在root两侧


if __name__ == "__main__":
    root = TreeNode(3)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(2)
    root.left, root.right = node1, node2
    node1.right = node3
    print(k_th_largest(root, 1))
