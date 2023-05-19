from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = {}
        for c in t:
            counts_t[c] = counts_t.setdefault(c, 0) + 1

        counts_s = defaultdict(int)
        in_window = 0
        total = len(counts_t)
        left, right = 0, 0
        min_length = float('inf')
        left_answer, right_answer = 0, 0

        while right < len(s):
            if s[right] in counts_t:
                counts_s[s[right]] += 1

                if counts_s[s[right]] == counts_t[s[right]]:
                    in_window += 1

            while left <= right and in_window == total:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    left_answer = left
                    right_answer = right

                if s[left] in counts_t:
                    counts_s[s[left]] -= 1

                    if counts_s[s[left]] < counts_t[s[left]]:
                        in_window -= 1
                left += 1
            right += 1

        if min_length == float('inf'):
            return ''
        return s[left_answer:right_answer + 1]