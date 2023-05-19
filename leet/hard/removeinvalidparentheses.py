# https://leetcode.com/problems/remove-invalid-parentheses/
from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()

        visited = {s}
        queue = deque()
        queue.append(s)

        def is_valid(expression: str) -> bool:
            counter = 0

            for c in expression:
                if c not in {'(', ')'}:
                    continue
                if c == '(':
                    counter +=1
                else:
                    counter -= 1
                if counter < 0:
                    return False
            return counter == 0

        while queue and len(result) == 0:
            for _ in range(len(queue)):
                expression = queue.popleft()

                if is_valid(expression):
                    result.add(expression)
                else:
                    for i in range(len(expression)):
                        if expression[i] not in '()':
                            continue

                        candidate = expression[:i] + expression[i + 1:]

                        if candidate not in visited:
                            visited.add(candidate)
                            queue.append(candidate)
        return list(result)

