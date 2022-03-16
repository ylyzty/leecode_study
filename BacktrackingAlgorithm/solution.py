"""
@Author: Lzy
@Time: 2022/03/07
@Description: 回溯问题
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if exist_dfs(i, j, 0, board, word):
                return True
    return False


def exist_dfs(row: int, col: int, index: int, board: List[List[str]], word: str) -> bool:
    if (not 0 <= row < len(board)) or (not 0 <= col < len(board[0])) \
            or board[row][col] != word[index]:
        return False

    if index == len(word) - 1:
        return True

    board[row][col] = ''  # 标记已经访问过的元素
    res = exist_dfs(row + 1, col, index + 1, board, word) or exist_dfs(row, col + 1, index + 1, board, word) \
          or exist_dfs(row - 1, col, index + 1, board, word) or exist_dfs(row, col - 1, index + 1, board, word)
    board[row][col] = word[index]
    return res


# 宽度优先搜索
def moving_count(m: int, n: int, k: int) -> int:
    """
    Offer 13. 机器人的运动范围
    :param m:
    :param n:
    :param k:
    :return:
    """
    queue, visited = [(0, 0, 0, 0)], set()
    while queue:
        i, j, sum_i, sum_j = queue.pop(0)
        if i >= m or j >= n or sum_i + sum_j > k or (i, j) in visited:
            continue
        visited.add((i, j))
        queue.append((i + 1, j, sum_i + 1 if (i + 1) % 10 != 0 else sum_i - 8, sum_j))
        queue.append((i, j + 1, sum_i, sum_j + 1 if (j + 1) % 10 != 0 else sum_j - 8))
    return len(visited)


# 深度优先搜索
def moving_count_2(m: int, n: int, k: int) -> int:
    visited = set()

    def dfs(i, j, sum_i, sum_j):
        if i >= m or j >= n or sum_i + sum_j > k or (i, j) in visited:
            return 0
        visited.add((i, j))
        return 1 + dfs(i + 1, j, sum_i + 1 if (i + 1) % 10 != 0 else sum_i - 8, sum_j) \
               + dfs(i, j + 1, sum_i, sum_j + 1 if (j + 1) % 10 != 0 else sum_j - 8)

    return dfs(0, 0, 0, 0)


def number_sum(num: int) -> int:
    res = 0
    while not num:
        res += num % 10
        num = num // 10
    return res


if __name__ == "__main__":
    print(moving_count_2(1, 2, 1))
