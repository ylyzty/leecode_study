from typing import List


def mei_tuan_002():
    n = int(input())  # 读入货物的数量
    weigh = list(map(int, input().split(" ")))
    fetch = list(map(int, input().split(" ")))
    res = []

    # 暴力求解
    for index in fetch:
        weigh[index - 1] = 0
        res.append(calculate_weight(weigh))
    print(res)


def calculate_weight(weigh: List[int]):
    max_weigh, index = 0, 0
    while index < len(weigh):
        if index < len(weigh) and weigh[index] == 0:
            index += 1
        if index < len(weigh) and weigh[index] != 0:
            temp = 0
            while index < len(weigh) and weigh[index] != 0:
                temp += weigh[index]
                index += 1
            max_weigh = max(max_weigh, temp)
    return max_weigh


if __name__ == "__main__":
    mei_tuan_002()