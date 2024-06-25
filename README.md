#About

The Sudoku puzzle can be viewed as a constraint satisfaction problem --  a mathematical question defined as a set of objects whose state must satisfy a number of constraints or limitations. 
The puzzle board can be seen as 81 variables in total, i.e. the tiles to be filled with digits. Each variable is named by its row and its column, and must be assigned a value from 1 to 9, subject to the constraint 
that no two cells in the same row, column, or box may contain the same value.

This project aims is to build a Sudoku puzzle solver implementing the AC3 and Backtracking Search algorithms.

#To Test

The tester class contains an example of a solved sudoku puzzle where the board is represented as a string of numbers. To try it out for yourself, you can choose any example from the sudoku_start.txt and use it as the input
in main(). The corresponding correct answer for the puzzle will be in sudoku_finish.txt
