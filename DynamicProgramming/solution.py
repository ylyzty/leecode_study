from typing import List


def fib(n: int) -> int:
    """
    Offer 10-I 斐波那契数列
    :param n:
    :return:
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007


def fib_2(n: int) -> int:
    a = [0, 1]
    for i in range(1, n):
        a.append(a[i - 1] + a[i])
    print(a)
    return a[n] % 100000007


def num_ways(n: int) -> int:
    """
    Offer 10-II 青蛙跳台阶问题
    :param n:
    :return:
    """
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def max_profit(prices: List[int]) -> int:
    """
    Offer63 股票最大利润
    :param prices:
    :return:
    """
    if not prices:
        return 0

    res = [0]
    cheapest = prices[0]
    for i in range(1, len(prices)):
        res.append(max(prices[i] - cheapest, res[i - 1]))
        cheapest = min(cheapest, prices[i])
    return res[len(prices) - 1]


def max_sub_array(nums: List[int]) -> int:
    """
    Offer 42. 连续子数组的最大和
    :param nums:
    :return:
    """
    if not len(nums):
        return 0
    res = [nums[0]]
    for i in range(1, len(nums)):
        res.append(max(res[i - 1] + nums[i], nums[i]))
    return max(res)


def max_value(grid: List[List[int]]) -> int:
    """
    Offer 47. 礼物的最大价值
    :param grid:
    :return:
    """
    row, col = len(grid), len(grid(0))
    values = [[0 for x in range(col)] for y in range(row)]
    values[0][0] = grid[0][0]
    for i in range(1, col):
        values[0][i] = values[0][i - 1] + grid[0][i]
    for j in range(1, row):
        values[i][0] = values[i - 1][0] + grid[i][0]

    for i in range(1, row):
        for j in range(1, col):
            values[i][j] = max(values[i - 1][j], values[i][j - 1]) + grid[i][j]

    return values[row - 1][col - 1]


def translate_num(num: int) -> int:
    """
    Offer 46. 把数字翻译成字符串
    :param num:
    :return:
    """
    # dp[i]只和dp[i-1]有关, 所以可以省略dp列表
    s_num = str(num)
    a, b = 1, 1
    for i in range(1, len(s_num)):
        a, b = a, (a + b if "10" <= s_num[i - 1:i + 1] <= "25" else b)
    return b


def length_of_longest_substring(s: str) -> int:
    """
    Offer 48. 最长不含重复字符的子字符串
    :param s:
    :return:
    """
    if len(s) <= 1:
        return len(s)

    dic = {}
    dp = [0 for _ in range(len(s))]
    dp[0], dic[s[0]] = 1, 0
    for i in range(1, len(s)):
        index = dic.get(s[i], -1)
        if dp[i - 1] < i - index:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = i - index

        dic[s[i]] = i  # 更新哈希表
    return max(dp)


def length_of_longest_substring_2(s: str) -> int:
    """
    节省 O(N)的 dp 空间
    :param s:
    :return:
    """
    dic = {}
    res, temp = 0, 0
    for i in range(len(s)):
        index = dic.get(s[i], -1)
        if temp < i - index:
            temp += 1
        else:
            temp = i - index
        dic[s[i]] = [i]
        res = max(res, temp)
    return res


def last_remaining(self, n: int, m: int):
    """
    Offer 62. 圆圈中最后剩下的数字
    """
    x = 0
    for i in range(2, n + 1):
        x = (x + m) % i
    return x


def nth_ugly_number(n: int) -> int:
    """
    动态规划
    Offer 49. 丑数
    初始状态：dp[0] = 1
    转移方程：dp[i] = min(n2, n3, n5)
    """
    dp = [1 for _ in range(n)]
    a, b, c = 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            a += 1
        if dp[i] == n3:
            b += 1
        if dp[i] == n5:
            c += 1
    return dp[-1]


if __name__ == "__main__":
    print(num_ways(39))
