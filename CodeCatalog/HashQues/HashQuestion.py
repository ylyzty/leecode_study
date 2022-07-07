<<<<<<< HEAD
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


class FourSumCount:
    """
    LeeCode 454: 四数相加 II
    """

    def solution(self, nums1, nums2, nums3, nums4) -> int:
        dict = {}
        for i in nums1:
            for j in nums2:
                dict[i + j] = dict.get(i + j, 0) + 1

        res = 0
        for i in nums3:
            for j in nums4:
                if -(i + j) in dict:
                    res += dict.get(-(i + j))

        return res


class CanConstruct:
    def solution(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for ch in magazine:
            dict[ch] = dict.get(ch, 0) + 1
        for ch in ransomNote:
            dict[ch] = dict.get(ch, 0) - 1
            if dict.get(ch) < 0:
                return False
        return True


class ThreeSum:
    def solution(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        if len(nums) < 3 or nums[0] > 0:
            return res

        for index in range(len(nums)):
            if nums[index] > 0:
                return res

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            temp, left, right = nums[index], index + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s > -temp:
                    right -= 1
                elif s < -temp:
                    left += 1
                else:
                    res.append([temp, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


class FourSum:
    def solution(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return res

        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if 4 * nums[i] > target:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + 3 * nums[j] > target:
                    break

                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left, right = left + 1, right - 1
        return res


if __name__ == "__main__":
    nums = [1, -2, -5, -4, -3, 3, 3, 5]
    test = FourSum()
    print(test.solution(nums, -11))
