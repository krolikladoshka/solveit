# https://leetcode.com/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        self.cash = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cash:
            self.cash[message] = timestamp
            return True
        else:
            if timestamp - self.cash[message] >= 10:
                self.cash[message] = timestamp
                return True
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
