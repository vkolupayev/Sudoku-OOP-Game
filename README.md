Sudoku, originally called Number Place) is a logic-based,
combinatorial number-placement puzzle.
The objective is to fill a 9×9 grid with digits so that:
each column, each row, and each of the nine 3×3 subgrids
that compose the grid (also called "boxes", "blocks", or "regions")
contain all of the digits from 1 to 9.
The puzzle setter provides a partially completed grid,
which for a well-posed puzzle has a single solution.

This project consists of a single Python script:
- sudoku.py

It uses a recursive backtracking algorithm to generate the sudoku board.
First it fills the grid then it removes the cells one by one.
Until it removes enough cells to form a grid of a desirable difficulty.
The algorithm makes sure to generate a valid grid.

Then you can play(instructions are given).