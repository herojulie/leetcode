from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        MAX_LEN = 9

        def get_box_number(r: int, c: int) -> int:
            if 0 <= r <= 2 and 0 <= c <= 2:
                return 0
            elif 0 <= r <= 2 and 3 <= c <= 5:
                return 1
            elif 0 <= r <= 2 and 6 <= c <= 8:
                return 2
            elif 3 <= r <= 5 and 0 <= c <= 2:
                return 3
            elif 3 <= r <= 5 and 3 <= c <= 5:
                return 4
            elif 3 <= r <= 5 and 6 <= c <= 8:
                return 5
            elif 6 <= r <= 8 and 0 <= c <= 2:
                return 6
            elif 6 <= r <= 8 and 3 <= c <= 5:
                return 7
            elif 6 <= r <= 8 and 6 <= c <= 8:
                return 8

        boxes = [set() for _ in range(MAX_LEN)]
        rows = [set() for _ in range(MAX_LEN)]
        cols = [set() for _ in range(MAX_LEN)]

        for r in range(MAX_LEN):
            for c in range(MAX_LEN):
                if board[r][c] == '.':
                    continue

                box = get_box_number(r, c)
                if board[r][c] in boxes[box]:
                    return False
                else:
                    boxes[box].add(board[r][c])

                if board[r][c] in rows[r]:
                    return False
                else:
                    rows[r].add(board[r][c])

                if board[r][c] in cols[c]:
                    return False
                else:
                    cols[c].add(board[r][c])

        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku(board=
                                   [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                       , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                       , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                       , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                       , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                       , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                       , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                       , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                       , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
