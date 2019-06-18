'''
Quest:
    According to the Wikipedia's article: "The Game of Life, also known simply as Life,
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
    using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Write a function to compute the next state (after one update) of the board given its current state.
    The next state is created by applying the above rules simultaneously to every cell in the current state,
    where births and deaths occur simultaneously.

    Example:

        Input:
        [
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
        ]
        Output:
        [
          [0,0,0],
          [1,0,1],
          [0,1,1],
          [0,1,0]
        ]

    Follow up:
    Could you solve it in-place? Remember that the board needs to be updated at the same time:
    You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite,
    which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Solution:
    - calculate sum around one cell: <2, = 2 or 3, >3
    - use transmission statues: 2 (from 0 to 1) and 3 (from 1 to 0)
    - then transfer 2 to 1 and 3 to 0
'''


class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        M, N = len(board), len(board[0])

        if M == 0 or N == 0:
            return None

        for m in range(M):
            for n in range(N):
                neighborSum = sum([board[i][j]%2 for i in range(m-1, m+2) for j in range(n-1, n+2) if 0 <= i < M and 0 <= j < N]) - board[m][n]
                if board[m][n] == 1 and (neighborSum > 3 or neighborSum < 2):
                    board[m][n] = 3
                if board[m][n] == 0 and neighborSum == 3:
                    board[m][n] = 2

        for m in range(M):
            for n in range(N):
                if board[m][n] == 2:
                    board[m][n] = 1
                elif board[m][n] == 3:
                    board[m][n] = 0

test = Solution()
x = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
test.gameOfLife(x)
print(x)