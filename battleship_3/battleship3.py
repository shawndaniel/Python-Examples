__author__ = 'Shawn Daniel'

import battleship


board_small = []
board_large = []
total_turns = 0
win_state_change = 0

# assign battleship boards with a number as the board reference and size of board
board_one = battleship.Board(board_small, 1, 3)
board_two = battleship.Board(board_large, 2, 5)
all_boards = board_one, board_two

player_one = battleship.Player('Bob', 0, 0)
player_two = battleship.Player('Tim', 0, 0)


def load_game():
    """Start from a fresh slate"""
    map(lambda x: x.reset(), all_boards)
    board_one.build_board()
    board_two.build_board()
    map(lambda x: x.show_board(), all_boards)
    b1_col, b1_row = board_one.gen_ships()
    b2_col, b2_row = board_two.gen_ships()
    return {
        'board_one': (b1_col, b1_row),
        'board_two': (b2_col, b2_row)
    }

ship_points = load_game()


def player_turns():
    if total_turns % 2 == 1:
        return player_one
    else:
        return player_two


def play_again():
    """if user wants to play again, restart / reload game"""
    global total_turns
    global ship_points
    answer = str(raw_input("Would you like to play again?"))
    if answer == "yes":
        total_turns = 0    # reset / start over from player one again
        ship_points = load_game()
    else:
        exit()


def best_out_of(win_state, player):
    """check the game statistics"""
    global total_turns
    if win_state == 1 and player.wins < 2:  # only do a check if player one the current game
        print "%s wins this game!" % player.name
        play_again()
    elif total_turns == 6:
        if win_state != 0:
            print "This match was a draw"
            play_again()
        else:
            play_again()
    elif player.wins >= 2:     # check who won best out of 3
        print "%s wins best out of 3" % player.name
        play_again()
    elif player.loses >= 2:
        print "%s lost best out of 3" % player.name
        play_again()
    else:
        play_again()


def input_check(ship_row, ship_col, player, board, board_size):
    """check/handle the players guesses of the ship points"""
    global win_state_change
    guess_col = 0
    guess_row = 0
    while True:
        try:
            guess_row = int(raw_input("Guess Row:")) - 1
            guess_col = int(raw_input("Guess Col:")) - 1
        except ValueError:
            print "Enter a number only."
            continue
        else:
            break
    match = guess_row == ship_row - 1 and guess_col == ship_col - 1
    not_on_board = (guess_row < 0 or guess_row > board_size - 1) \
                   or (guess_col < 0 or guess_col > board_size - 1)
    if match:
        win_state_change = 1  # notes that someone has won the current game
        player.wins += 1
        print "Congratulations! You sunk my battleship!"
        best_out_of(win_state_change, player)
        map(lambda x: x.show_board(), all_boards)
    elif not_on_board:
        print "Oops, that's not even in the ocean."
        map(lambda x: x.show_board(), all_boards)
    elif board[guess_row][guess_col] == "X":
        print "You guessed that one already."
        map(lambda x: x.show_board(), all_boards)
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        win_state_change = 0
        map(lambda x: x.show_board(), all_boards)
    return win_state_change


"""Start the game logic"""
for games in range(3):
    games += 1  # 3 games total
    for turns in range(6):  # 6 turns total = 3 turns for each player
        total_turns += 1
        if player_turns() == player_one:
            print "It's %ss turn" % player_one.name
            input_check(
                ship_points['board_one'][0],
                ship_points['board_one'][1],
                player_one, board_one.board, board_one.size
            )
        elif player_turns() == player_two:
            print "It's %ss turn" % player_two.name
            input_check(
                ship_points['board_two'][0],
                ship_points['board_two'][1],
                player_two, board_two.board, board_two.size
            )
        else:
            break
        if total_turns == 6 and player_turns() == player_one:
            best_out_of(win_state_change, player_one)
        elif total_turns == 6 and player_turns() == player_two:
            best_out_of(win_state_change, player_two)
        else:
            continue
    if games == 3:
            print "The game has ended."
            exit()
    else:
        continue
