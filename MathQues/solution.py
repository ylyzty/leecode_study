"""
@Author: Lzy
@Time: 2022/03/16
@Description: 数学问题
"""


class Solution:
    def find_nth_digit(self, n: int) -> int:
        """
        Offer 44. 数字序列中某一位的数字
        """
        width, start, count = 1, 1, 9
        while n > count:
            n -= count
            width += 1
            start *= 10
            count = 9 * start * width
        num = start + (n - 1) // width    # 确定是哪个数字
        res = str(num)[(n - 1) % width]   # 确定在数字的第几位
        return int(res)
