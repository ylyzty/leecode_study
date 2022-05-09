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


# @Tag: 归并排序
class ReversePairs:
    """
    Offer 51. 数组中的逆序对
    利用归并排序的过程记录逆序对数
    """
    @staticmethod
    def reverse_pairs(nums: List[int]) -> int:
        temp = [0] * len(nums)
        return ReversePairs.merge_sort(nums, 0, len(nums) - 1, temp)

    @staticmethod
    def merge_sort(nums, left, right, temp):
        if left >= right:
            return 0
        mid = (left + right) // 2

        count = ReversePairs.merge_sort(nums, left, mid, temp) + ReversePairs.merge_sort(nums, mid + 1, right, temp)

        i, j = left, mid + 1
        pos = left
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[pos] = nums[i]
                i += 1
                # count += j - mid - 1
            else:
                temp[pos] = nums[j]
                j += 1
                count += mid - i + 1
            pos += 1
        for k in range(i, mid + 1):
            temp[pos] = nums[k]
            # count += j - mid - 1
            pos += 1
        for k in range(j, right + 1):
            temp[pos] = nums[k]
            pos += 1

        nums[left: right + 1] = temp[left: right + 1]
        return count


if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    print(ReversePairs.reverse_pairs(nums))
