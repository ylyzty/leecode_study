"""
@Author: Lzy
@Time: 2022/03/09
@Description: 动态规划
"""

class Solution:

    def last_remaining(self, n: int, m: int):
        """
        Offer 62. 圆圈中最后剩下的数字
        """
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
