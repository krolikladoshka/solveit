# https://leetcode.com/problems/design-browser-history/
from collections import deque


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = 0
        self.last = 0
        self.pages = [homepage]

    def visit(self, url: str) -> None:
        self.current += 1

        if self.current < len(self.pages):
            self.pages[self.current] = url
        else:
            self.pages.append(url)
        self.last = self.current

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.pages[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.last, self.current + steps)
        return self.pages[self.current]


class BrowserHistory1:
    def __init__(self, homepage: str):
        self.current = homepage
        self.stack = deque()
        self.forward_deq = deque()

    def visit(self, url: str) -> None:
        self.stack.append(self.current)
        self.current = url
        self.forward_deq.clear()

    def back(self, steps: int) -> str:
        while self.stack and steps > 0:
            self.forward_deq.append(self.current)
            self.current = self.stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while self.forward_deq and steps > 0:
            self.stack.append(self.current)
            self.current = self.forward_deq.pop()
            steps -= 1
        return self.current
