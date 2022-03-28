from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0:
            return False

        queue = deque([0])
        unlocked = set([0])
        while queue:
            room_no = queue.popleft()
            for key in rooms[room_no]:
                if key in unlocked:
                    continue
                queue.append(key)
                unlocked.add(key)

        return True if len(rooms) == len(unlocked) else False


if __name__ == '__main__':
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
