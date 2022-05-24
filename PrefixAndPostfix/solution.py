"""
@Author: Lzy
@Time: 2022/04/05
@Description: 前缀和、后缀和
"""
from typing import List


class Solution:
    def construct_arr(self, a: List[int]) -> List[int]:
        """
        Offer 66. 构建乘积数组
        """
        prefix, postfix = [1 for i in range(len(a))], [1 for i in range(len(a))]
        for i in range(1, len(a)):
            prefix[i] = prefix[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * a[i + 1]

        for i in range(len(a)):
            a[i] = prefix[i] * postfix[i]
        return a
