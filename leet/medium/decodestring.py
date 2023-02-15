# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        res = []

        def parse_number(start: int) -> (int, int):
            end = start
            while s[end].isdigit():
                end += 1

            return int(s[start:end]), end

        def decode_pattern(start: int) -> (str, int):
            pattern = []
            k, end = parse_number(start)
            i = end + 1
            while s[i] != ']':
                c = s[i]
                if c.isdigit():
                    subpattern, end = decode_pattern(i)
                    i = end + 1
                    pattern.append(subpattern)
                else:
                    pattern.append(c)
                    i += 1
            pattern = ''.join(pattern)

            res = []
            for j in range(k):
                res.append(pattern)
            return ''.join(res), i

        i = 0
        while i < len(s):
            c = s[i]
            if not c.isdigit():
                res.append(c)
                i += 1

                continue
            pattern, end = decode_pattern(i)
            res.append(pattern)
            i = end + 1
        return ''.join(res)
