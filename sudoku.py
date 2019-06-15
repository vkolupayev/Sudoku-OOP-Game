# Sudoku game OOP

from random import randint, shuffle
import os
os.system('')

class Sudoku:

    def __init__(self):
        self.counter = 0
        self.grid = []
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.form = []
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        self.form.append([True, True, True, True, True, True, True, True, True])
        
    def printGrid(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.form[row][col]:
                    print(self.grid[row][col], end = ' ')
                else:
                    print('\033[1m' + str(self.grid[row][col]) + '\033[0m', end = ' ')
            print()
        print()
            
    def setForm(self):
        for row in range(0,9):
            for cell in range(0, 9):
                if self.grid[row][cell] !=0:
                    self.form[row][cell] = False
            
    def checkGrid(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.grid[row][col]==0:
                    return False
        #We have a complete grid!  
        return True 
        
    def countGrid(self):
        count = 0
        for row in self.grid:
            for cell in row:
                if cell != 0:
                    count+=1
        return count     
     
    def saveGrid(self, filename):
        outputFile = open(filename, 'w')
        
        for row in self.grid:
            for cell in row:
                print(cell, file = outputFile, end = ' ')
            print(file = outputFile)
            
        for row in self.form:
            for cell in row:
                print(cell, file = outputFile, end = ' ')
            print(file = outputFile)
            
        outputFile.close()
            
    def loadGrid(self, filename):
        inputFile = open(filename, "r")
        
        self.grid.clear()
        self.form.clear()
        
        line_num = 1
        
        for line in inputFile:
            if line_num <=9:
                cells_string = line.split() # Split the line on runs of whitespace
                cells = [int(c) for c in cells_string] # Convert to integers
                self.grid.append(cells) # Add the "row" to your list.
            else:
                cells_string = line.split() # Split the line on runs of whitespace
                cells = [c == 'True' for c in cells_string] # Convert to integers
                self.form.append(cells) # Add the "row" to your list.
            line_num +=1
        
        inputFile.close()
     
    #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solveGrid(self, grid):
        #Find next empty cell
        for i in range(0,81):
            row=i//9
            col=i%9
            if grid[row][col]==0:
                for value in range (1,10):
                    #Check that this value has not already be used on this row
                    if not(value in grid[row]):
                        #Check that this value has not already be used on this column
                        if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                            #Identify which of the 9 squares we are working on
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[grid[i][6:9] for i in range(6,9)]
                            #Check that this value has not already been used in this group 3x3
                            if not value in (square[0] + square[1] + square[2]):
                                grid[row][col]=value
                                for row in range(0,9):
                                    for col in range(0,9):
                                        if grid[row][col]==0:
                                            a = False
                                        else:
                                            a = True
                                    #Complete grid
                                
                                if a:
                                    self.counter+=1
                                    break
                                else:
                                    if self.solveGrid(grid):
                                        return True
                break
        grid[row][col]=0 

    #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def fillGrid(self):
        numberList=[1,2,3,4,5,6,7,8,9]
        #Find next empty cell
        for i in range(0,81):
            row=i//9
            col=i%9
            if self.grid[row][col]==0:
                shuffle(numberList)      
                for value in numberList:
                    #Check that this value has not already been used on this row
                    if not(value in self.grid[row]):
                        #Check that this value has not already been used on this column
                        if not value in (self.grid[0][col],self.grid[1][col],self.grid[2][col],self.grid[3][col],self.grid[4][col],self.grid[5][col],self.grid[6][col],self.grid[7][col],self.grid[8][col]):
                            #Identify which of the 9 squares we are working on
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(6,9)]
                            #Check that this value has not already been used in this group 3x3
                            if not value in (square[0] + square[1] + square[2]):
                                self.grid[row][col]=value
                                if self.checkGrid():
                                    return True
                                else:
                                    if self.fillGrid():
                                        return True
                break
        self.grid[row][col]=0 
        
    def genGameGrid(self, diff): 
        while self.countGrid()>diff:
            #Select a random cell that is not already empty
            row = randint(0,8)
            col = randint(0,8)
            while self.grid[row][col]==0:
                row = randint(0,8)
                col = randint(0,8)
            #Remember its cell value in case we need to put it back  
            backup = self.grid[row][col]
            self.grid[row][col]=0
  
            #Take a full copy of the grid
            copyGrid = []
            for r in range(0,9):
                copyGrid.append([])
                for c in range(0,9):
                    copyGrid[r].append(self.grid[r][c])
    
            #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
            self.counter=0
            self.solveGrid(copyGrid)   
            #If the number of solutions is different from 1 then we need to cancel the change by putting the value we took away back in the grid
            if self.counter!=1:
                self.grid[row][col]=backup
               
class Game:

    def __init__(self):
        difficulty = {"easy": 40, "medium": 35, "hard": 30, "test":80}
        print(difficulty)
        self.gameDiff = self.chooseDifficulty()
        sudoku = Sudoku()
        sudoku.fillGrid()
        sudoku.saveGrid("filledFile.txt")
        #Take a full copy of the grid
        winningGrid = []
        for r in range(0,9):
            winningGrid.append([])
            for c in range(0, 9):
                winningGrid[r].append(sudoku.grid[r][c])
        sudoku.genGameGrid(difficulty[self.gameDiff])
        sudoku.setForm()
        sudoku.saveGrid("saveFile.txt")
        sudoku.printGrid()
        self.play(sudoku, winningGrid)

    def chooseDifficulty(self):
        while True:
            userInput = input("Enter difficulty(easy, medium, hard): ")

            if userInput.lower() == "easy" or userInput.lower() == "medium" or userInput.lower() == "hard" or userInput.lower() == "test":
                return userInput.lower()
            else:
                print("Only easy, medium, hard #test# allowed! ")
                continue

    def play(self, sudoku, win):
        while not self.gameStatus(sudoku, win):
            try:
                userInput = int(input("Enter command(1 - input, 2 - solve, 3 - exit): "))
            except ValueError:
                print("Invalid input!")
                continue
            if userInput == 1:
                self.inputCell(sudoku, win)
                sudoku.printGrid()
            elif userInput == 2:
                for row in win:
                    for cell in row:
                        print(cell, end=' ')
                    print()
                print("Better luck next time")
                break
            elif userInput == 3:
                exit()

        print("Congragulations, you have completed the puzzle!!!")

    def gameStatus(self, sudoku, winGrid):
        if sudoku.grid == winGrid:
            return True
        else:
            return False

    def inputCell(self, sudoku, win):

        while True:
            while True:
                try:
                    row = int(input("Enter row(1-9): "))
                except ValueError:
                    print("Invalid input.")
                    continue

                if row < 1 or row > 9:
                    print("Choose row from 1-9")
                    continue
                else:
                    break

            while True:
                try:
                    col = int(input("Enter column(1-9): "))
                except ValueError:
                    print("Invalid input.")
                    continue

                if col < 1 or col > 9:
                    print("Choose column from 1-9")
                    continue
                else:
                    break

            if not sudoku.form[row-1][col-1]:
                print("You can not change base cells, choose a different one")
                continue

            while True:
                try:
                    val = int(input("Enter value(1-9): "))
                except ValueError:
                    print("Invalid input.")
                    continue

                if val < 1 or val > 9:
                    print("Choose value from 1-9")
                    continue
                else:
                    break

            if val == win[row-1][col-1]:
                sudoku.grid[row-1][col-1] = val
                break
            else:
                print("Inncorect, try again!")
                continue
       
game = Game()
