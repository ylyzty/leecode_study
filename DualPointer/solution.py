"""
@Author: Lzy
@Time: 2022/03/05
@Description: 双指针问题
"""
from typing import List


def exchange(nums: List[int]) -> List[int]:
    """
    Offer 21. 调整数组顺序使奇数位于偶数前面
    :param nums:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left < right:
        # x&1位运算的结果判断奇偶
        while left < right and nums[left] & 1 == 1:
            left += 1
        while left < right and nums[left] & 1 == 0:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
    return nums


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Offer 57. 和为 s 的两个数字
    :param nums:
    :param target:
    :return:
    """
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            return [nums[i], nums[j]]
    return []


def reverse_words(s: str) -> str:
    """
    Offer 58. 翻转单词顺序
    :param s:
    :return:
    """
    res = s.split()
    return ' '.join(res[::-1])


if __name__ == "__main__":
    print(reverse_words("the sky  is   blue"))
