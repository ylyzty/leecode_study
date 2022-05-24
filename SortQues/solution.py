"""
@Author: Lzy
@Time: 2022/03/09
@Description: 排序问题
"""
import functools
from typing import List
from heapq import *


def min_number(nums: List[int]) -> str:
    """
    Offer 45. 把数组排成最小的数
    核心思想：自定义排序规则
    x + y < y + x; 则 x 应该放在 y 的左边，即 x 比 y 小
    :param nums:
    :return:
    """

    def quick_sort(left: int, right: int):
        if left >= right:
            return
        i, j = left, right
        while i < j:
            while num_to_str[j] + num_to_str[left] >= num_to_str[left] + num_to_str[j] and i < j:
                j -= 1
            while num_to_str[i] + num_to_str[left] <= num_to_str[left] + num_to_str[i] and i < j:
                i += 1
            num_to_str[i], num_to_str[j] = num_to_str[j], num_to_str[i]
        num_to_str[left], num_to_str[i] = num_to_str[i], num_to_str[left]
        quick_sort(left, i - 1)
        quick_sort(i + 1, right)

    """
    Python3自定义排序规则
    """

    def my_compare(str1: str, str2: str):
        if str1 + str2 > str2 + str1:
            return 1
        elif str1 + str2 < str2 + str1:
            return -1
        else:
            return 0

    num_to_str = [str(num) for num in nums]
    num_to_str.sort(key=functools.cmp_to_key(mycmp=my_compare))
    print(num_to_str)
    quick_sort(0, len(nums) - 1)
    return "".join(num_to_str)


def is_straight(nums: List[int]) -> bool:
    nums.sort()
    for num in nums:
        if num == 0:
            continue
        else:
            minimum = num
    return True if nums[4] - minimum < 5 else False


def get_least_numbers(arr: List[int], k: int) -> List[int]:
    """
    Offer 40. 最小的 k 个数
    :param arr:
    :param k:
    :return:
    """
    if k >= len(arr):
        return arr

    def quick_sort(left: int, right: int):
        """返回前 k 小的数"""
        i, j = left, right
        while i < j:
            while i < j and arr[left] <= arr[j]:
                j -= 1
            while i < j and arr[i] <= arr[left]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[i] = arr[i], arr[left]

        if k < i:
            return quick_sort(left, i - 1)
        if k > i:
            return quick_sort(i + 1, right)
        return arr[:k]

    return quick_sort(0, len(arr) - 1)


class MedianFinder:
    def __init__(self):
        self.min_heap = []  # 小顶堆，保存较大的一半数据
        self.max_heap = []  # 大顶堆，保存较小的一半数据，保存负的

    def add_num(self, num: int):
        if len(self.min_heap) != len(self.max_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))

    def find_median(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


class ReorderLogFiles:
    def solution(self, logs: List[str]) -> List[str]:
        dig_log, let_log = [], []
        for i in range(len(logs)):
            temp = logs[i].split(' ', 1)[1]
            temp = temp.replace(' ', '')
            if temp.isdigit():
                dig_log.append(logs[i])
            else:
                let_log.append(logs[i])
        let_log.sort(key=functools.cmp_to_key(mycmp=self.compare))
        let_log.extend(dig_log)
        return let_log

    def compare(self, log1: str, log2: str):
        split_log1 = log1.split(' ', 1)
        split_log2 = log2.split(' ', 1)
        if split_log1[1] == split_log2[1]:
            return -1 if split_log1[0] < split_log2[0] else 1
        else:
            return -1 if split_log1[1] < split_log2[1] else 1


if __name__ == "__main__":
    # print(min_number([2, 20, 21, 10]))
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    reorder_log = ReorderLogFiles()
    print(reorder_log.solution(logs))
