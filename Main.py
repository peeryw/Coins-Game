# CS 461
# Professor Brian Hare
# Program 1
# Due 3 Spet. 2017
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

# def get_file(output):
#     try:
#         items = [output.strip().lower().split("")]
#         if items[0] == int:
#             number_coins_int = items[0]
#             print(number_coins_int, '\n')
#     except ValueError:
#         print("\n Could not convert argument to int \n", items)
print ("Game of Coins\n")

while True:



    print ("What file would you like to load?")
    print ("Selection is: \n" "odd_coins.txt, simple_coins.txt, us_coins.txt ")

    open_file_str = input("Open which file?\n")

    try:
        file_str = open (open_file_str.lower(),'r')
        #with open(open_file_str.lower(),'r') as output:
        #    coins_value_list = list(output.split(''))
        output = file_str
        coins_value_list = output.readlines()
        coins_value_list

    except IOError:
        print ("The file", open_file_str, "doesn't exist.")
        print ("Program now closing.")
        exit()#kill program

   # coins_value_list = [output.readlines()]
    #number_of_coins = coins_value_list[0].remove
    #print ("Number of coins for game is", number_of_coins)
    print (coins_value_list)#testing purposes

    file_str.close()
    exit()