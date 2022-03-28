from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0

        perfect_squares = [i * i for i in range(1, 100)]
        if n in perfect_squares:
            return 1

        queue = deque([n])
        ans = 1

        while queue:
            size = len(queue)
            while size > 0:
                current_num = queue.popleft()
                res = []
                for i in range(len(perfect_squares)):
                    if current_num - perfect_squares[i] == 0:
                        return ans
                    elif current_num - perfect_squares[i] > 0:
                        res.append(current_num - perfect_squares[i])
                    else:
                        queue.extend(reversed(res))
                        break
                size -= 1
            ans += 1
        return -1

    def numSquares2(self, n: int) -> int:
        def isPerfectSquare(n):
            square_n = int(n ** 0.5)
            return square_n * square_n == n

        if isPerfectSquare(n):
            return 1
        else:
            nq = int(n ** 0.5)
            for i in range(nq + 1):
                if isPerfectSquare(n - i ** 2):
                    return 2
        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4
        else:
            return 3


if __name__ == '__main__':
    print(Solution().numSquares2(13))
