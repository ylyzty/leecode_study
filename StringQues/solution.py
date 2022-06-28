from typing import List


class Solution:
    @staticmethod
    def str_to_int(str: str) -> int:
        temp = []
        flag = True
        INT_MAX, INT_MIN = pow(2, 31) - 1, pow(-2, 31)
        for i in range(len(str)):
            if flag and str[i].isspace():
                continue
            if flag and (str[i] == "+" or str[i] == "-"):
                temp.append(str[i])
                flag = False
            elif str[i].isdigit():
                temp.append(str[i])
                flag = False
            else:
                break

        res = ''.join(temp)
        if len(res) == 1 and (res[0] == '+' or res[0] == '-'):
            res = 0
        res = int(res) if res else 0
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res

    @staticmethod
    def is_match(s: str, p: str) -> bool:
        """
        Offer 19. 正则表达式匹配
        @Method: 动态规划
        """
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        # 初始化
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        # 转移方程
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    elif dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                        dp[i][j] = True
        return dp[-1][-1]

    @staticmethod
    def is_match_recursion(s: str, p: str) -> bool:
        """
        Offer 19. 正则表达式匹配
        @Method: 递归实现, 时间复杂度高
        """
        if not s:
            if len(p) % 2 != 0:
                return False
            for i in range(1, len(p), 2):
                if p[i] != '*':
                    return False
            return True

        if not p:
            return False

        i, j, ch = 0, 0, 'a'
        if j + 1 < len(p):
            ch = p[j + 1]
        if ch != '*':
            if s[i] == p[j] or p[j] == '.':
                return Solution.is_match_recursion(s[i + 1:], p[j + 1:])
            else:
                return False
        else:
            if s[i] == p[j] or p[j] == '.':
                return Solution.is_match_recursion(s[i + 1:], p) or Solution.is_match_recursion(s, p[j + 2:])
            else:
                return Solution.is_match_recursion(s, p[j + 2:])


"""
LeeCode双周赛: 2022/05/28
"""
def largestWordCount(messages: List[str], senders: List[str]) -> str:
    max_words = 0
    max_sender = ""
    dict = {}

    for index, sender in enumerate(senders):
        message = messages[index]
        length = len(message.split(' '))
        dict[sender] = dict.setdefault(sender, 0) + length
        if dict[sender] == max_words:
            max_sender = max(sender, max_sender)
        if dict[sender] > max_words:
            max_words = dict[sender]
            max_sender = sender
    return max_sender, max_words


def maximumImportance(n: int, roads: List[List[int]]) -> int:
    temp = [0 for _ in range(n)]
    for road in roads:
        temp[road[0]] += 1
        temp[road[1]] += 1
    temp.sort()
    weigh = [i for i in range(1, n + 1)]

    res = 0
    for i in range(n):
        res += weigh[i] * temp[i]
    return res

