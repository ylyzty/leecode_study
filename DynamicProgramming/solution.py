from typing import List


class Solution:
    @staticmethod
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

    @staticmethod
    def fib_2(n: int) -> int:
        a = [0, 1]
        for i in range(1, n):
            a.append(a[i - 1] + a[i])
        print(a)
        return a[n] % 100000007

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def last_remaining(n: int, m: int):
        """
        Offer 62. 圆圈中最后剩下的数字
        """
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x

    @staticmethod
    def dices_probability(n: int) -> List[float]:
        dp = [[0 for j in range(n)] for i in range(6 * n)]
        for i in range(6):
            dp[i][0] = 1
        for j in range(1, n):
            for i in range(j, 6 * (j + 1)):
                count = 1
                while i - count >= 0 and count <= 6:
                    dp[i][j] += dp[i - count][j - 1]
                    count += 1
        res = []
        for i in range(n-1, 6*n):
            res.append(dp[i][n-1])
        for i in range(len(res)):
            res[i] /= pow(6, n)
        return res


if __name__ == "__main__":
    print(Solution.dices_probability(2))
