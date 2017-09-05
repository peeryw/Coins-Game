# CS 461
# Professor Brian Hare
# Program 1
# Due 3 Sept. 2017
# Scott Peery

# Coins Game

# A simple game consisting of a series of n coins (n is even) of various denominations
# laid out in a row. (For our purposes, the denominations do not match any actual real-
# world coins, but all have a value greater than 0.) Two players take turns, alternating
# removing a coin from either end of the row and keeping the coin so removed. Play
# continues until all coins are removed; the object is to end with a higher total
# value than the opponent.

# Ask user for file to load
# Load file
# Read file info
#      the file only contains ints
#      first int is number of coins
#      remaining ints are the values of each coin to be displayed on the game board

# Once file has been read, do the computations necessary to find the expected score
# and the best choice to make, then play interactively with the user

# show the row of coins
# ask user to select either left or right coin (L or R)
# remove coin
# update score for player on screen
# update display for coins left on board
# tell user the AI's selection for coin
# update score for AI
# update display for coins left on board
# loop these actions till all coins gone
# display who won and final scores

#  Display a short report documenting the code and explain how the search was implemented
# and handled the game logic.

play = True
coin_list = []
move = 0
player_score = []
ai_score = []
game_state = dict()
valid_move = str
turn = str


def welcome_message():
    print("""
    ------------------------------------------------------------
                             COINS
    ------------------------------------------------------------
    Rules:
        1. Player always moves first
        2. You can only choose 1 coin at a time
        3. Legal moves are either the coin on the left end 
            of the board or the right end of the board
        4. Each time a coin is chosen, the value amount is added
            to your total score
        5. The game ends when all the coins are gone
        6. The winner is whom ever has the highest total of coin
         values
    ------------------------------------------------------------
    """)


def winner():
    global play
    if len(coin_list) == 0:
        if player_score > ai_score:
            print("Player wins!")
            play = False
            return play
        elif ai_score > player_score:
            print("AI wins. Better luck next time.")
            play = False
            return play
        else:
            print("Somehow you tied.")
            play = False
            return play
    else:
        return


# function to determine winning moves for AI
def ai_strategy(coin_list, start, end):
    # import the global variable for valid move
    global valid_move
    # check that the end index is not less than the start index
    # if it is, end game
    if start > end:
        return 0
    # define variables looking from start of list and end of list
    front_strategy = str(coin_list[start])
    back_strategy = str(coin_list[end])
    # for strategy taking coin from start of list
    try:
        # look one move forward from left side of list
        if coin_list[start+1] < coin_list[end]:
            result_front_strategy = front_strategy + str(ai_strategy(coin_list, start+1, end-1))
        else:
            result_front_strategy = front_strategy + str(ai_strategy(coin_list, start+2, end))
    # handle the index error that occurs at end of game for last coin in list
    except IndexError:
        valid_move = "front"
        return valid_move
    # for strategy taking coin from back of list
    try:
        # look one move forward from the right side of the list
        if coin_list[start] < coin_list[end-1]:
            result_back_strategy = back_strategy + str(ai_strategy(coin_list, start, end-2))
        else:
            result_back_strategy = back_strategy + str(ai_strategy(coin_list, start+1, end-1))
    # handle the index error that occurs at end of game for last coin in list
    except IndexError:
        valid_move = "front"
        return valid_move
    # compare each strategy and save the move that yields best result
    if result_front_strategy > result_back_strategy:
        game_state[(start, end)] = result_front_strategy
        valid_move = "back"
        return valid_move
    else:
        game_state[(start, end)] = result_back_strategy
        valid_move = "front"
        return valid_move


# print game board
def game_board():
    # number of coins currently available
    score()
    print(coin_list,"\n")


# determine who's move it is
def whos_turn():
    global move, turn
    if move % 2 == 0:
        turn = "player"
        return turn
    else:
        turn = "ai"
        return turn


# player turn
def players_turn():
    # get input from player
    global move, valid_move
    print("Players turn to choose.")
    player_move = input("Which coin would you like?\nEnter L for left coin or R for right coin.\n").lower()
    if player_move == "r":
        valid_move = player_move
        move += 1
        player_score.append(coin_list.pop())
        game_board()
        return move
    elif player_move == 'l':
        valid_move = player_move
        move +=1
        player_score.append(coin_list.pop(0))
        game_board()
        return move
    else:
        print("Invalid move.")
        players_turn()
        return


# AI's turn
def ai_turn():
    global move, valid_move
    # run ai strategy()
    ai_strategy(coin_list, 0, len(coin_list)-1)
    # get result from game_state
    print("AI's turn to choose.")
    if valid_move == "front":
        # remove left coin, update ai score
        print("AI chooses left coin\n.")
        ai_score.append(coin_list.pop(0))
        game_board()
        # update move
        move += 1
        return move
    elif valid_move == "back":
        # remove right coin, update ai score
        print("AI chooses right coin.\n")
        ai_score.append(coin_list.pop())
        game_board()
        # update move
        move +=1
        return move


# update score board
def score():
    print("Player   AI")
    print(sum(player_score), "      ", sum(ai_score))


def main():
    global play
    while play == True:
        welcome_message()
        # ask user for file
        print ("What file would you like to load?")
        print ("Selection is: \n" "odd_coins.txt, simple_coins.txt, us_coins.txt ")
        open_file_str = input("Open which file? Please include '.txt' in file name\n")

        # check that file exist, handle errors, and put ints into a list
        try:
            with open(open_file_str.lower(), 'r')as f:
                for line in f:
                    for s in line.split(' '):
                        coin_list.append(int(s))
            # get number of coins game should be using
            number_of_coins = coin_list.pop(0)

            # check that number of coins needed for game is in the list
            # first number in list from file gives this value
            if len(coin_list) != number_of_coins:
                print("Game file is corrupt.Missing correct number of coins.")
                exit()

        except IOError:
            print("The file", open_file_str, "doesn't exist.")
            print("Program now closing.")
            exit()  # kill program

        game_board()

        while len(coin_list) !=0:
            whos_turn()
            if turn == "player":
                players_turn()
            elif turn == "ai":
                ai_turn()
        if len(coin_list) == 0:
            if sum(player_score) > sum(ai_score):
                print("Player wins")
                print(sum(player_score), "to ",sum(ai_score))
                exit()
            elif sum(player_score) == sum(ai_score):
                print("You have ended in a tie.")
                print(sum(player_score), "to ", sum(ai_score))
                play = False
            else:
                print("AI wins")
                print(sum(ai_score), "to ", sum(player_score))
                play = False

# start game
if __name__ == "__main__":
    main()


