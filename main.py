#Script that solves a sudoku given a board.

#1 solution : the NaiVe wich tries every single combination of numbers in order to make the solution work. => SLOW AND TAKE A LOT OF RESSOURCE
#sudoku uses 9 numbers in 9 square divide in 9 rows and 9 columns
#WE HAVE 9 POSSIBILITIES IN 81 SQUARE => 9^81 POSSIBILITIES

#2 solution = Bactracking
#Pick an empty square => try all number => if number found fits, we switch to another case and repeat => FASTER
#As soon the solution cannot be complete => backtrack and keep trying until the number fit and make the solution work


board = [
		      [3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check if row is valid
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if colunm is valid
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check if box is valid
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for o in range(box_x * 3, box_x*3 + 3):
            if bo[i][o] == num and (i,o) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for o in range(len(bo[0])):
            if o % 3 == 0 and o != 0:
                print(" ¦ ", end="")

            if o == 8:
                print(bo[i][o])
            else:
                print(str(bo[i][o]) + " ", end="")


def find_empty(bo):
	for i, row in enumerate(bo):
	    for o, val in enumerate(row):
	        if val == 0:
	            return (i, o)
	return None

print_board(board)
solve(board)
print("___________________ \nAND HERE IS THE SOLUTION : ")
print_board(board)
