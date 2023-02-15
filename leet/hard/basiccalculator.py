# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        operands = []
        values = []

        def parse_number(i) -> (int ,int):
            res = []
            while i < len(s) and s[i].isdigit():
                res.append(s[i])
                i += 1
            return int(''.join(res)), i

        def eval_parentheses(i):
            token = s[i]
            while i < len(s) and token != ')':
                pass

        res = 0
        sign = 1
        index = 0
        while index < len(s):
            token = s[index]

            if token.isdigit():
                value, index = parse_number(index)
                res += sign * value
                operands.append(res)
            elif token == '+':
                pass
                # res += sign *
            elif token == '-':
                operands.append(token)
            elif token.isdigit():
                number, index = parse_number(index)
                values.append(number)


        return values[0]