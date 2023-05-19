# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self):
        self.alphabet = 26
        self.nodes = [None] * self.alphabet
        self.is_word = False

    def put(self, c: str):
        self.nodes[ord(c) - ord('a')] = TrieNode()

    def get(self, c: str):
        return self.nodes[ord(c) - ord('a')]

    def exists(self, c: str):
        return self.get(c) is not None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for i, c in enumerate(word):
            if not node.get(c):
                node.put(c)
            node = node.get(c)
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for i, c in enumerate(word):
            c_node = node.get(c)

            if not c_node:
                return False
            node = c_node
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for i, c in enumerate(prefix):
            c_node = node.get(c)
            if not c_node:
                return False
            node = c_node
        return True
