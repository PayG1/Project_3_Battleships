# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from random import randint

""" The sea reperesents the board of the game """

sea = []

""" Made the board more spacious"""
for i in range(8):
    sea.append(["~"] * 7)


def print_sea(sea):
    for row in sea:
        print("  ".join(row))

print("Wake up! We are being attacked, you are the only one who can use the cannons.\
\nUse the cannonballs and hit the  enemy ship.")
print_sea(sea)

""" Calculates a random row and column """


def rand_row(sea):
    return randint(0, len(sea) - 1)


def rand_column(sea):
    return randint((0), len(sea) - 1)

""" Added Ships  """

ship_row = rand_row(sea)
ship_column = rand_column(sea)
second_ship_row = rand_row(sea)
second_ship_column = rand_column(sea)
list_1 = [ship_row, ship_column]
list_2 = [second_ship_row, second_ship_column]

""" Loop for the player to keep trying to hit the ship """

for guess in range(8):
    print('guess', guess+1)
    guess_row = int(input("Guess row:"))-1
    guess_column = int(input("Guess column:"))-1

    if (guess_row == ship_row and guess_column == ship_column)\
            or (guess_row == second_ship_row and guess_column == second_ship_column):
        print("Nice shot! We can escape now")
        break
    
    else:
        if (guess_row < 0 or guess_row > 7) \
                or (guess_column < 0 or guess_column > 7):
            print("Where are you aiming at, Focus!")
        elif(sea[guess_row][guess_column] == "x"):
            print ("You have already tried that location, go again.")
        else:
            print("That was close, keep trying")
            sea[guess_row][guess_column] = "x"
    if guess == 7:
        print("Wait, we are out of cannonballs? It's game over.")
    print_sea(sea)
