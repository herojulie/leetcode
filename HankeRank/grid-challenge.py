#!/bin/python3

def my_sort(sample: str) -> str:
    temp = [c for c in sample]
    temp.sort()
    return ''.join(temp)


def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = my_sort(grid[i])

    for i in range(len(grid[0])):
        prev = grid[0][i]
        for j in range(1, len(grid)):
            if prev > grid[j][i]:
                return 'NO'
            prev = grid[j][i]
    return 'YES'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
