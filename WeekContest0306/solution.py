from typing import List


def cells_in_range(s: str) -> List[str]:
    a, b = s.split(':')
    col_len = ord(b[0]) - ord(a[0])
    row_len = ord(b[1]) - ord(a[1])
    print(col_len, row_len)
    res = []
    for i in range(col_len + 1):
        col = chr(ord(a[0]) + i)
        for j in range(row_len + 1):
            row = chr(ord(a[1]) + j)
            res.append("".join([col, row]))
    return res


def minimal_k_sum(nums: List[int], k: int) -> int:
    res, flag = 0, 0
    nums.sort(reverse=False)
    print(nums)
    for i in range(1, k+1):
        res += i
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] <= k + flag:
            flag += 1
            res += k + flag - nums[i]
    return res


if __name__ == "__main__":
    a = minimal_k_sum([96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52,
                       19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84], 35)
    print(a)