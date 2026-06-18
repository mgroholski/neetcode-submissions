'''
We need to check if any of the conditions are invalid:

1. A row contains a duplicate digit
2. A column contains duplicate digit
3. Square contains duplicate digit

Make sets of each subcomponent and check when adding

How to index the squares?

(0-2, 0-2) - 0
(3-5, 0-2) - 1
(6-8, 0-2) - 2
(0-2, 3-5) - 3
(3-5, 3-5) - 4
(6-8, 3-5) - 5

(j // 3) * 3 + i // 3

'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        N_sqrt = int(N ** (1/2))

        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        squares = [set() for _ in range(N)]

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != ".":
                    if val in rows[i]:
                        return False
                    rows[i].add(val)

                    if val in columns[j]:
                        return False
                    columns[j].add(val)

                    square_idx = ((j // N_sqrt) * N_sqrt) + (i // N_sqrt)
                    if val in squares[square_idx]:
                        return False
                    squares[square_idx].add(val)

        return True
                







        