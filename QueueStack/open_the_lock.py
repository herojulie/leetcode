from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set(deadends)
        numberOfTurns = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                current_lock = queue.popleft()
                if current_lock == target: return numberOfTurns
                if current_lock in visited: continue
                visited.add(current_lock)

                res = []
                for i, ch in enumerate(current_lock):
                    num = int(ch)
                    res.append(current_lock[:i] + str((num - 1) % 10) + current_lock[i + 1:])
                    res.append(current_lock[:i] + str((num + 1) % 10) + current_lock[i + 1:])
                queue.extend(res)

            numberOfTurns += 1
        return -1


if __name__ == '__main__':
    print(Solution().openLock(
        ["5557", "5553", "5575", "5535", "5755", "5355", "7555", "3555", "6655", "6455", "4655", "4455", "5665", "5445",
         "5645", "5465", "5566", "5544", "5564", "5546", "6565", "4545", "6545", "4565", "5656", "5454", "5654", "5456",
         "6556", "4554", "4556", "6554"], "5555"))
