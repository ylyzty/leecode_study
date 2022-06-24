from typing import List
import numpy as np

"""
代码随想录: 数组部分
"""


class RemoveElement:
    """
    移除元素
    """

    def __init__(self):
        print("Create an instance of class RemoveElement.")

    def remove_element(self, nums: List[int], val: int) -> int:
        """
        LeeCode 27: 移动元素
        方法: 双指针
        时间复杂度: O(N)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        # 由于while循环的条件设置为 i<=j, 所以最后 i 的值始终等于 len(新数组)
        return left

    def move_zeroes(self, nums: List[int]) -> None:
        """
        LeeCode 283: 移动零
        方法: 双指针
        时间复杂度: O(N)
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return None

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        LeeCode 26 删除数组中的重复项目
        方法: 快慢指针
        时间复杂度: 0(N)
        """
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


class OrderedArray:
    def __init__(self):
        print("Create an instance of OrderedArray.")

    def sorted_squares(self, nums: List[int]) -> List[int]:
        """
        LeeCode 977: 有序数组的平方
        方法：(二分查找) + 双指针
        时间复杂度：O(N)
        """
        res = []
        index = self.get_index(nums)

        res.append(pow(nums[index], 2))
        i, j = index - 1, index + 1
        while i >= 0 and j <= len(nums) - 1:
            if abs(nums[i]) <= abs(nums[j]):
                res.append(pow(nums[i], 2))
                i -= 1
            else:
                res.append(pow(nums[j], 2))
                j += 1

        while i >= 0:
            res.append(pow(nums[i], 2))
            i -= 1
        while j <= len(nums) - 1:
            res.append(pow(nums[j], 2))
            j += 1

        return res

    def get_index(self, nums: List[int]):
        """
        获取平方值最小的 index
        """
        for i in range(len(nums) - 1):
            if abs(nums[i]) < abs(nums[i + 1]):
                return i
        return len(nums) - 1


class SubArray:
    def __init__(self):
        print("Create an instance of SubArray.")

    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        res, prefix = len(nums) + 1, nums[0]
        i, j = 0, 1
        while j <= len(nums):
            if prefix < target and j == len(nums):
                break
            if prefix < target:
                prefix += nums[j]
                j += 1
            else:
                res = min(res, j - i)
                prefix -= nums[i]
                i += 1
        return res if res != (len(nums) + 1) else 0

    def min_sub_array_len_2(self, target, nums):
        """
        LeeCode 209: 长度最小的子数组
        方法: 双指针、滑动窗口
        时间复杂度: 0(N)
        """
        res = len(nums) + 1
        left, right = 0, 0
        s = 0
        while right < len(nums):
            s += nums[right]
            while s >= target:
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1
        return res if res != (len(nums) + 1) else 0


class GenerateMatrix:
    def __init__(self):
        print("Create an instance of GenerateMatrix.")

    def spiral_matrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index = 0
        row, col = 0, 0

        res = [[0 for _ in range(n)] for _ in range(n)]
        for num in range(1, pow(n, 2) + 1):
            res[row][col] = num
            (dx, dy) = directions[index]
            new_row, new_col = row + dx, col + dy

            # res[new_row][new_col] > 0 表示 new_row, new_col 已经填充过
            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n or res[new_row][new_col] > 0:
                index = (index + 1) % 4
                (dx, dy) = directions[index]
            row, col = row + dx, col + dy

        return res


class BookMyShow:
    """
    Question: 超出时间限制
    Method: 线段树
    """
    def __init__(self, n, m):
        self.seat = np.array([[0 for _ in range(m)] for _ in range(n)])
        self.m = m
        self.n = n

    def gather(self, k, maxRow) -> List[int]:
        for i in range(maxRow + 1):
            for j in range(self.m - k + 1):
                if np.sum(self.seat[i, j:j+k]) == 0:
                    while k > 0:
                        k -= 1
                        self.seat[i][j+k] = 1
                    return [i, j]
        return []

    def scatter(self, k, maxRow) -> bool:
        if np.sum(self.seat[:maxRow+1, :]) <= self.m * (maxRow + 1) - k:
            count = 0
            for i in range(self.m * (maxRow + 1)):
                if self.seat[i // self.m, i % self.m] == 0:
                    count += 1
                    self.seat[i // self.m, i % self.m] = 1

                if count >= k:
                    break
            return True

        return False

if __name__ == "__main__":
    # bms = BookMyShow(2, 5)
    # print(bms.gather(4, 0))
    # print(bms.gather(2, 0))
    # print(bms.scatter(5, 1))
    # print(bms.scatter(5, 1))
    g = GenerateMatrix()
    print(g.spiral_matrix(3))
