"""
@Author: Lzy
@Time: 2022/03/16
@Description: 数学问题
"""


class Solution:
    def find_nth_digit(self, n: int) -> int:
        width, start, count = 1, 1, 9
        while n > count:
            n -= count
            width += 1
            start *= 10
            count = 9 * start * width
        num = start + (n - 1) // width
        res = str(num)[(n - 1) % width]
        return res
