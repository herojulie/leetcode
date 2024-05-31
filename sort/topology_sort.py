from collections import deque


class TopologySort:
    def __init__(self, nNode: int, edges: list[list[int, int]]):
        self.nNode = nNode
        self.indegree = [0] * nNode
        self.node_map = self.create_map(edges)

    def create_map(self, edges: list[list[int, int]]):
        node_map = {}
        for i in range(self.nNode):
            node_map[i] = list()
        for edge in edges:
            src, dst = edge[0], edge[1]
            node_map[src].append(dst)
            self.indegree[dst] += 1
        return node_map

    def do(self) -> list:
        ans = []
        queue = deque()
        for i in range(len(self.indegree)):
            if self.indegree[i] == 0:
                queue.append(i)

        while queue:
            now = queue.popleft()
            ans.append(now)

            for i in self.node_map[now]:
                self.indegree[i] -= 1
                if self.indegree[i] == 0:
                    queue.append(i)

        return ans


if __name__ == '__main__':
    edges = [[0, 1],
             [0, 4],
             [1, 2],
             [1, 5],
             [2, 3],
             [3, 6],
             [4, 5],
             [5, 3]]
    print(TopologySort(nNode=7, edges=edges).do())
