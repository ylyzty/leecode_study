class ReplaceSpace:
    def solution(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == ' ':
                res.append('%20')
            else:
                res.append(ch)
        return ''.join(res)


class ReverseWords:
    def solution(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

    def solution2(self, s: str) -> str:
        s = s.strip()
        i, j = len(s) - 1, len(s)
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1:j])
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i + 1
        return ' '.join(res[::-1])


class RepeatedSubstringPattern:
    def solution(self, s: str) -> bool:
        return s in (s + s)[1:-1]

    def solution2(self, s: str) -> bool:
        # 枚举子串长度
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                flag = True
                for j in range(i, len(s)):
                    if s[j] != s[j - i]:
                        flag = False
                        break

                if flag:
                    return True
        return False


if __name__ == "__main__":
    test = ReverseWords()
    test.solution2(" Hello World ")
