# https://leetcode.com/problems/word-ladder
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_length = len(beginWord)

        graph = defaultdict(list)

        for word in wordList:
            for i in range(word_length):
                graph[word[:i] + '*' + word[i + 1:]].append(word)

        start = beginWord
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            candidate, steps = queue.popleft()

            if candidate == endWord:
                return steps + 1

            for i in range(word_length):
                candidate_node = candidate[:i] + '*' + candidate[i + 1:]

                for child in graph[candidate_node]:
                    if child in seen:
                        continue
                    queue.append((child, steps + 1))
                    seen.add(child)
        return 0
