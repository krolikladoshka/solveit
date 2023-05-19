from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicted_s1 = defaultdict(int)
        for c in s1:
            dicted_s1[c] += 1

        window = len(s1)
        permutation = defaultdict(int)
        for i in range(len(s2)):
            permutation[s2[i]] += 1
            if i >= window:
                if permutation[s2[i - window]] == 1:
                    permutation.pop(s2[i - window])
                else:
                    permutation[s2[i - window]] -= 1
            if permutation == dicted_s1:
                return True
        return False
