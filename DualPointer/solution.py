"""
@Author: Lzy
@Time: 2022/03/05
@Description: 双指针问题
"""
from typing import List
from collections import deque
from queue import Queue


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


def find_continuous_sequence(target: int) -> List[List[int]]:
    """
    Offer 57-II. 和为s的连续正数序列
    滑动窗口法
    """
    left, right, temp, res = 1, 2, 3, []
    while left < right:
        if temp == target:
            res.append(list(range(left, right + 1)))
        if temp >= target:
            temp -= left
            left += 1
        else:
            right += 1
            temp += right
    return res


def max_sliding_window(nums: List[int], k: int) -> int:
    if not nums:
        return []
    res = []
    window = Queue()
    value = deque()
    for i in range(k):
        window.put(nums[i])
        while value and value[-1] < nums[i]:
            value.pop()
        value.append(nums[i])
    res.append(value[0])
    # i, j = 0, k
    while k < len(nums):
        num = window.get()
        if num == value[0]:
            value.popleft()
        window.put(nums[k])
        while value and value[-1] < nums[k]:
            value.pop()
        value.append(nums[k])
        res.append(value[0])
        k += 1
    return res


def diStringMatch(s: str) -> List[int]:
    res = [i for i in range(len(s) + 1)]
    left, right = 0, 1
    while right < len(res):
        i, j = left, right
        while i >= 0 and ((s[i] == 'I' and res[i] > res[j]) or (s[i] == 'D' and res[i] < res[j])):
            res[i], res[j] = res[j], res[i]
            i, j = i - 1, j - 1
        left, right = left + 1, right + 1
    return res


def diStringMatch_2(s: str) -> List[int]:
    """
    LeeCode 942 增减字符串匹配
    Tag: 贪心选择
        - 如果当前字母s[i] == 'I', 则 res[i] = low 取可使用的最小值
        - 如果当前字母s[i] == 'D', 则 res[i] = high 取可使用的最大值
    """
    low, high = 0, len(s)
    res = [0 for i in range(len(s) + 1)]
    for i, c in enumerate(s):
        if c == 'I':
            res[i] = low
            low += 1
        else:
            res[i] = high
            high -= 1
    res[len(s)] = low    # 最后一个元素时low = high
    return res


if __name__ == "__main__":
    s = "DDI"
    print(diStringMatch(s))
