from typing import List


class RemoveElement:
    """
    代码随想录: 数组部分
    """
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

    def remove_duplicates(self, nums:List[int]) -> int:
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
