from functools import lru_cache


class Solution:
    def isHappy2(self, n: int) -> bool:
        def get_next(number) -> int:
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

    def isHappy3(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        turtle = n
        rabbit = get_next(n)

        while rabbit != 1 and turtle != rabbit:
            turtle = get_next(n)
            rabbit = get_next(get_next(rabbit))
        return rabbit == 1

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x)**2 for x in str(n)])
        return n == 1


if __name__ == '__main__':
    print(Solution().isHappy(3))
