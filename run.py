# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from random import randint

""" The sea reperesents the board of the game """

sea = []

""" Made the board more spacious"""
for i in range(8):
    sea.append(["~"] * 8)

def print_sea(sea):
    for row in sea:
        print ("  ".join(row))

print("Wake up! We are being attacked, you are the only one who can use the cannons.\nWe have 10 cannon balls left, try your best to hit the 4 enemy ships.")
print_sea(sea)

""" Calculates a random row and column """


def rand_row(sea):
    return randint(0, len(sea) - 1)

def rand_column(sea):
    return randint((0), len(sea) - 1)


