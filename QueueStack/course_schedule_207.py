# https://leetcode.com/problems/course-schedule/

from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = list()
        graph = dict()
        indegrees = [0] * numCourses

        for course in range(numCourses):
            graph[course] = list()

        for after, prior in prerequisites:
            indegrees[after] += 1
            graph[prior].append(after)

        q = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            ans.append(now)

            for n in graph[now]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)

        print(ans)
        return len(ans) == numCourses


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))
