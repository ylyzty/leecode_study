from LeeCode.TreeQues import TreeNode


def level_order(root):
    if not root:
        return []
    res, queue = [], []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def mirror_tree(root: TreeNode):
    """
    Offer 27 二叉树的镜像
    :param root:
    :return:
    """
    if not root:
        return []

    nodes = [root]
    while nodes:
        node = nodes.pop(0)
        node.left, node.right = node.right, node.left
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return root


def mirror_tree_2(root: TreeNode):
    """
    递归
    :param root:
    :return:
    """
    if not root:
        return
    root.left, root.right = mirror_tree_2(root.right), mirror_tree_2(root.left)
    return root


def is_symmetric(root: TreeNode):
    """
    Offer28. 对称的二叉树
    递归
    :param root:
    :return:
    """

    def recur(L: TreeNode, R: TreeNode):
        if not L and not R:
            return True
        if not L or not R or L.val != R.val:
            return False
        return recur(L.left, R.right) and recur(L.right, R.left)

    return recur(root.left, root.right) if root else True


def is_sub_structure(A: TreeNode, B: TreeNode):
    """
    Offer 26. 树的子结构
    :param A:
    :param B:
    :return:
    """

    def recur(L, R):
        if not R:
            return True
        if not L or L.val != R.val:
            return False
        return recur(L.left, R.left) and recur(L.right, R.right)

    if not B:
        return True
    if not A or A.val != B.val:
        return False

    return bool(A and B) and \
           (recur(A, B) or is_sub_structure(A.left, B) or is_sub_structure(A.right, B))


if __name__ == '__main__':
    pass
