# 栈与队列问题


"""
LeeCode 232
使用两个栈实现先入先出队列
"""
from typing import List


class MyQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)

    def pop(self) -> int:
        if (not self.stackA) and (not self.stackB):
            return None

        if self.stackB:
            return self.stackB.pop()

        while self.stackA:
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

    def peek(self) -> int:
        res = self.stackB.pop()
        self.stackB.append()
        return res

    def empty(self) -> bool:
        if (not self.stackA) and (not self.stackB):
            return True

        return False


"""
LeeCode 20
有效的括号
"""


class IsValid:
    def solution(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                peek = stack.pop()
                if ch == ')' and peek != '(':
                    return False
                elif ch == '}' and peek != '{':
                    return False
                elif ch == ']' and peek != '[':
                    return False
                else:
                    continue
        return not stack


"""
LeeCode 1047
删除字符串中的所有相邻重复项
"""


class RemoveDuplicates:
    def solution(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                peek = stack[-1]
                if peek == c:
                    stack.pop()
                    continue
                else:
                    stack.append()
        return ''.join(stack)


"""
LeeCode 150
逆波兰表达式求值
"""


class EvalRPN:
    def solution(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                data1 = stack.pop()
                data2 = stack.pop()
                if token == '+':
                    stack.append(data2 + data1)
                elif token == '-':
                    stack.append(data2 - data1)
                elif token == '*':
                    stack.append(data2 * data1)
                elif token == '/':
                    stack.append(int(data2 / data1))
                else:
                    print("Unknown Condition.")
                    return 0
        return stack.pop()


if __name__ == "__main__":
    test = EvalRPN()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(test.solution(tokens))