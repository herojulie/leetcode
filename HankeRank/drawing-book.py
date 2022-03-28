#!/bin/python3

def pageCount(n, p):
    # Write your code here
    total_pages = (n + 1) // 2 if n % 2 == 0 else n // 2
    for page in range(total_pages + 1):
        left = page * 2
        right = left + 1
        if left == p or right == p:
            return page if page <= (total_pages - page) else total_pages - page


if __name__ == '__main__':
    print(pageCount(5, 3))
