from typing import List

class Solution:
  """
  Class representing a solution to count the number of islands in a given matrix.
  Args:
  ----
  matrix : List[List[int]]
      A 2D list representing the matrix.

  Methods:
  -------
  is_island(matrix: List[List[int]], row_idx: int, col_idx: int) -> None:
      Recursive function to mark and explore the neighbors of an island.

  count_islands(matrix: List[List[int]]) -> int:
      Function to count the number of islands in the matrix.
  """

  def is_island(self, matrix: List[List[int]], row_idx: int, col_idx: int) -> None:
      """
      Recursive function to mark and explore the neighbors of an island.

      Args:
      ----
      matrix : List[List[int]]
          A 2D list representing the matrix.

      row_idx : int
          The row index of the island to be marked.

      col_idx : int
          The column index of the island to be marked.

      Returns:
      -------
      None
      """
      rows = len(matrix)
      cols = len(matrix[0])

      if row_idx < 0 or col_idx < 0 or row_idx >= rows or col_idx >= cols or matrix[row_idx][col_idx] != 1:
          return None
      
      matrix[row_idx][col_idx] = "X"
      self.is_island(matrix, row_idx+1, col_idx)
      self.is_island(matrix, row_idx, col_idx+1)
      self.is_island(matrix, row_idx-1, col_idx)
      self.is_island(matrix, row_idx, col_idx-1)

  def count_islands(self, matrix: List[List[int]]) -> int:
      """
      Function to count the number of islands in the matrix.

      Args:
      ----
      matrix : List[List[int]]
          A 2D list representing the matrix.

      Returns:
      -------
      count : int
          The number of islands in the matrix.
      """
      rows, cols = len(matrix), len(matrix[0])
      count = 0
      for row_idx in range(rows):
          for col_idx in range(cols):
              if matrix[row_idx][col_idx] == 1:
                  self.is_island(matrix, row_idx, col_idx)
                  count += 1
      return count
  
matrix =[[1, 1, 1, 1, 0], 
         [0, 0, 0, 1, 0], 
         [1, 1, 0, 0, 0], 
         [0, 0, 0, 0, 1]]
m=4
n=5

solution = Solution()
print(solution.count_islands(matrix, m, n))
print(matrix)