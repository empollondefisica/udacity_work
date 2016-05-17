# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(puzzle):
    max_value = len(puzzle)

    # check value range
    for row in puzzle:
        for elem in row:
            if elem > max_value or elem <= 0:
                return False

    # check count of elements in row
    for row in puzzle:
        count_row = []
        for index in range(0, max_value):
            count_row.append(0)
        for elem in row:
            count_row[int(elem) - 1] = count_row[int(elem) - 1] + 1
        for elem in count_row:
            if elem != 1:
                return False

    # check count of elements in columns
    for col_i in range(0, max_value):
        count_column = []
        for index in range(0, max_value):
            count_column.append(0)
        for row_i in range(0, max_value):
            index = puzzle[row_i][col_i]
            count_column[index - 1] = count_column[index - 1] + 1
        for elem in count_column:
            if elem != 1:
                return False

    return True

    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False



