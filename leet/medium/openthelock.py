class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def possible_turns(start: str):
            for i in range(4):
                for d in (-1, 1):
                    next_turn = (int(start[i]) + d) % 10
                    yield start[:i] + str(next_turn) + start[i + 1:]

        seen = set(deadends)

        if '0000' in seen:
            return -1
        seen.add('0000')
        queue = deque([('0000', 0)])

        while queue:
            guess, depth = queue.popleft()

            if guess == target:
                return depth

            for next_turn in possible_turns(guess):
                if next_turn not in seen:
                    seen.add(next_turn)
                    queue.append((next_turn, depth + 1))
        return -1
