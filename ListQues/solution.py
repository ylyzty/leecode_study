from typing import List

from ListQues import ListNode


def delete_node(head: ListNode, val: int) -> ListNode:
    """
    Offer 18. 删除链表的节点
    :param head:
    :param val:
    :return:
    """
    virtual = ListNode(0)
    virtual.next = head
    pre, cur = virtual, head
    while cur:
        if cur.val == val:
            pre.next = cur.next
            break
        else:
            pre, cur = cur, cur.next
    return virtual.next


def get_kth_from_end(head: ListNode, k: int) -> ListNode:
    """
    Offer 22. 链表中的倒数第 K 个节点
    :param head:
    :param k:
    :return:
    """
    left = head
    for _ in range(k):
        head = head.next
    right = head
    while right:
        left, right = left.next, right.next
    return left


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Offer 25. 合并两个排序的链表
    :param l1:
    :param l2:
    :return:
    """
    virtual = ListNode(0)
    cur = virtual
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2

    return virtual.next


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    nodeA, nodeB = headA, headB
    while nodeA != nodeB:
        nodeA = nodeA.next if nodeA else headB
        nodeB = nodeB.next if nodeB else headA
    return nodeA


def last_remaining(n: int, m: int) -> int:
    """
    Offer 62. 圆圈中最后剩下的数字
    动态规划
    """
    x = 0
    for i in range(2, n + 1):
        x = (x + m) % i


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Offer 29. 顺时针打印矩阵
        时间复杂度 O(mn)
        """
        if not matrix:
            return []

        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        res = []
        while True:
            for i in range(left, right):  # 从左至右
                res.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])  # 从上至下
            right -= 1
            if left >= right:
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])  # 从右至左
            bottom -= 1
            if top >= bottom:
                break
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left >= right:
                break
        return res

    def spiral_order_2(self, matrix: List[List[int]]) -> List[int]:
        """
        时间复杂度O(MN)
        空间复杂度O(MN)
        """
        if not matrix:
            return []

        res = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # 辅助矩阵, 表示未访问
        index = 0  # 当前方向
        row, column = 0, 0
        for i in range(len(matrix[0]) * len(matrix)):
            res.append(matrix[row][column])
            visited[row][column] = True
            next_row, next_column = row + directions[index][0], column + directions[index][1]
            if not (0 <= next_row < len(matrix) and 0 <= next_column < len(matrix[0]) and not visited[next_row][
                next_column]):
                index = (index + 1) % 4
            row += directions[index][0]
            column += directions[index][1]
        return res

    def validate_stack_sequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[index]:
                index += 1
                stack.pop()
        return False if stack else True


if __name__ == "__main__":
    test = Solution()
    print(test.spiral_order_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
