# https://leetcode.com/problems/longest-common-prefix

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        def common_prefix(s1: str, s2: str) -> str:
            i = 0
            for a, b in zip(s1, s2):
                if a != b:
                    break
                i += 1
            return s1[:i]

        prefix = strs[0]
        for s in strs:
            prefix = common_prefix(prefix, s)
        return prefix

    def longestCommonPrefix_nlong(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        longest_prefix = ''

        for j in range(1, len(strs)):
            if not strs[j].startswith(strs[0][:1]):
                return ''
            for k in range(1, len(strs[0]) + 1):
                if strs[j].startswith(strs[0][:k]):
                    longest_prefix = strs[0][:k]
                else:
                    break
        return longest_prefix

    def longestCommonPrefix_second(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        prefixes = {}

        for s in strs:
            for i in range(1, len(s) + 1):
                prefixes[s[:i]] = -1
        for prefix in prefixes:
            for s in strs:
                if s.startswith(prefix):
                    prefixes[prefix] += 1
        mx = 1
        for prefix, count in prefixes.items():
            if count >= mx:
                mx = count
        longest_prefixes = []
        for prefix, count in prefixes.items():
            if count == mx:
                longest_prefixes.append(prefix)

        longest_prefix = ''
        for prefix in longest_prefixes:
            if len(longest_prefix) < len(prefix):
                longest_prefix = prefix

        return longest_prefix
