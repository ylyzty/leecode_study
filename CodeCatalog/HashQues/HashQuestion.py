"""
代码随想录: 哈希表部分
"""
from typing import List


class IsAnagram:
    def __init__(self):
        pass

    """
    LeeCode 242: 有效的字母异位词
    """

    def solution(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr1 = [0 for _ in range(26)]
        arr2 = [0 for _ in range(26)]

        for c in s:
            arr1[ord(c) - ord('a')] += 1
        for c in t:
            arr2[ord(c) - ord('a')] += 1

        for i in range(26):
            if arr1[i] != arr2[i]:
                return False

        return True

    def solution2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            dict_s[s[i]] = dict_s.setdefault(s[i], 0) + 1
            dict_t[t[i]] = dict_t.setdefault(t[i], 0) + 1

        if len(dict_s) != len(dict_t):
            return False

        for key in dict_s.keys():
            if dict_s.get(key) != dict_t.get(key):
                return False
        return True


class Intersection:
    """
    LeeCode 349: 两个数组的交集
    """

    def solution(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))


class IsHappy:
    """
    LeeCode 202: 快乐数
    """

    def solution(self, n: int) -> bool:
        history = set()
        cur = self.getSquares(n)
        while cur != 1:
            if cur in history:
                return False
            history.add(cur)
            cur = self.getSquares(cur)
        return True

    def getSquares(self, n: int) -> int:
        s = 0
        while n:
            s += pow(n % 10, 2)
            n //= 10
        return s


class TwoSum:
    def solution(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            if dict.get(num) is not None:
                return [dict.get(num), index]
            else:
                dict[target - num] = index


if __name__ == "__main__":
    test = TwoSum()
    print(test.solution([2,7,11,15], 9))
