from typing import List


class Solution:
    @staticmethod
    def str_to_int(str: str) -> int:
        temp = []
        flag = True
        INT_MAX, INT_MIN = pow(2, 31) - 1, pow(-2, 31)
        for i in range(len(str)):
            if flag and str[i].isspace():
                continue
            if flag and (str[i] == "+" or str[i] == "-"):
                temp.append(str[i])
                flag = False
            elif str[i].isdigit():
                temp.append(str[i])
                flag = False
            else:
                break

        res = ''.join(temp)
        if len(res) == 1 and (res[0] == '+' or res[0] == '-'):
            res = 0
        res = int(res) if res else 0
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res


if __name__ == "__main__":
    print(Solution.str_to_int("+"))
