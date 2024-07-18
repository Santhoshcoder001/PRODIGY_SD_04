import tkinter as tk
from tkinter import messagebox

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.cells = [[tk.Entry(root, width=3, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5)

        solve_button = tk.Button(root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=4, pady=20)

        clear_button = tk.Button(root, text="Clear", command=self.clear)
        clear_button.grid(row=9, column=5, columnspan=4, pady=20)

    def get_grid(self):
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                val = self.cells[row][col].get()
                if val == '':
                    grid_row.append(0)
                else:
                    grid_row.append(int(val))
            grid.append(grid_row)
        return grid

    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    self.cells[row][col].delete(0, tk.END)
                else:
                    self.cells[row][col].delete(0, tk.END)
                    self.cells[row][col].insert(0, str(grid[row][col]))

    def solve(self):
        grid = self.get_grid()
        if solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

    def clear(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
