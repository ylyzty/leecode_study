"""
@Author: Lzy
@Time: 2022/03/16
@Description: Hash表
"""
from typing import List


class Solution:

    @staticmethod
    def majority_element(nums: List[int]) -> int:
        """
        Offer 39. 数组中出现次数超过一半的数字
        1、摩尔投票法
        2、哈希表统计法
        """
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x
