""" This is the original version of the battleship game that is created as the result of completing the "battleship" lesson from Codeacademy's Python course
    As you can see I also thoroughly commented the code for beginners to understand
"""

from random import randint

board = []
#1
# append the list item: ["O"] 5 times in 5 lists
for x in range(5):
    board.append(["O"] * 5)
#2
# for each list that is within the outer list (board), present the list elements seperated by spaces
def print_board(board):
    for row in board:
        print " ".join(row)
#3
# print the board using the print_board function
print "Let's play Battleship!"
print "1"
print_board(board)

# generate a random number between 0 and the length of the boards outer lists (0-5 = 6 actual numbers in computer terms) so therefore we must subtract one so that the output will actually count 5, in computer terms (0-1-2-3-4 = 5) thus generating a random row number that fits on teh board
def random_row(board):
    rand_number = randint(0, len(board) - 1)
# generate a random number between 0 and the length of the boards inner listed elements len(board[0])
def random_col(board):
    rand_number = randint(0, len(board[0]) - 1)
#6
# assign the ship_row variable a random row of the board list using the random_row function
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

#7
# give the user a range of 4 turns and start counting the turns each time the for loop runs
for turn in range(4):
    turn = turn + 1
    #store the users first and second numbers as an integers
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    #compare the users numbers with the random numbers that were previously generated, if it's the same, they win, then close the app.
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    # otherwise if the users guess is outside of the range of the boards rows and columns, print it's not even in ocean.
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            # also if the guess was already guessed previously, print already guessed
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            # if users guess isn't matching anything accounted for, clearly they missed and just replace the ["O"] at their guessed location with an "X" in the corresponding list elements within the board outer list
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # remaining code outside the if / else statements to let that code run first, but still within the for loop to keep count of each turn
        print turn + 1
        print_board(board)
        
        if turn == 3:
            print "Game Over"
            break