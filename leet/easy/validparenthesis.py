# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesises = {
            '(': ')', '[': ']', '{': '}'
        }
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if c != parenthesises[opening]:
                    return False
        return len(stack) == 0

    def isValid_slower(self, s: str) -> bool:
        stack = []
        parenthesises = {
            ')': '(', ']': '[', '}': '{',
        }
        for c in s:
            if c in parenthesises.values():
                stack.append(c)
            elif c in parenthesises.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] != parenthesises[c]:
                    return False
                stack.pop()
        return len(stack) == 0
