"""
@Author: Lzy
@Time: 2022/03/16
@Description: 位运算
"""
from typing import List


class Solution:

    def single_numbers(self, nums: List[int]) -> List[int]:
        """
        Offer56-I. 数组中数字出现的次数
        """
        a, b, x, y = 0, 1, 0, 0
        for i in range(len(nums)):
            a ^= nums[i]
        while a & b != 1:
            b <<= 1
        for i in range(len(nums)):
            if nums[i] & b:
                x ^= nums[i]
            else:
                y ^= nums[i]
        return [x, y]

    def single_numbers_2(self, nums: List[int]) -> int:
        """
        Offer56-II. 数组中数字出现的次数 II
        最优解法: 有限状态机位运算
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key, value in dict.items():
            if value == 1:
                return key
        return 0
