
def sum_up_to_n(n: int) -> int:
    """
    write a recursion function that given an input n
    sums all non-negative integers up to n
    """
    if n == 0:
        return 0
    
    return sum_up_to_n(n - 1) + n


def num_of_paths(n: int, m: int) -> int:
    """
    Write a function that takes two inputs n and m
    and outputs the number of unique paths from the top
    left corner to bottom right corner of a n X m grid.
    Constraints: you can only move down or right 1 unit at a time.
    """
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    
    return num_of_paths(n - 1, m) + num_of_paths(n, m - 1)


def num_of_ways_partition(n: int, m: int) -> int:
    """
    Write a function that counts the number of ways you can
    partition n objects using parts up to m (assuming m >= 0)
    """
    if n == 0:
        return 1
    if m <= 0:
        return 0
    return num_of_ways_partition(n, m - 1) + num_of_ways_partition(n - m, m)


print(sum_up_to_n(10))
print(num_of_paths(3, 3))
