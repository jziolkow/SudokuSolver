__author__ = 'jeffziolkowski'


# Puzzle27
# Each numbered box represents the 9 squares that should ultimately contain all digits in the range [1-9]
# The numbering sequence starts in the top-left and continues left-to-right, top-to-bottom
box1 = ((0, 0, 3), (5, 0, 9), (0, 0, 0))
box2 = ((0, 0, 0), (6, 0, 0), (0, 0, 0))
box3 = ((5, 2, 0), (0, 0, 8), (0, 9, 0))
box4 = ((6, 0, 7), (9, 0, 5), (8, 3, 2))
box5 = ((9, 0, 1), (8, 0, 3), (0, 0, 7))
box6 = ((0, 0, 5), (0, 4, 0), (9, 0, 0))
box7 = ((0, 8, 0), (0, 0, 6), (0, 0, 0))
box8 = ((0, 0, 0), (0, 0, 8), (4, 5, 2))
box9 = ((0, 0, 0), (0, 1, 0), (8, 7, 0))


# Group the numbered boxes so as to create collections that break the puzzle into horizontal thirds.
htop = (box1, box2, box3)
hmiddle = (box4, box5, box6)
hbottom = (box7, box8, box9)


# Group the numbered boxes so as to create collections that break the puzzle into vertical thirds.
vleft = (box1, box4, box7)
vmiddle = (box2, box5, box8)
vright = (box3, box6, box9)


# Add the groups to form the whole of the puzzle.  NOTE: The horizontal groupings were used arbitrarily;
# at this point, this has no impact other than driving the logic used to print the puzzle to the screen.
whole = (htop, hmiddle, hbottom)


# TODO: Implement loadpuzzle
def loadpuzzle():

    """
    Load a puzzle into the solver.

    Args:
        None

    Returns:
        None
    """
    print "TODO"

# TODO: Implement solvepuzzle
def solvepuzzle():

    """
    Solves the currently loaded puzzle.

    Args:
        None
    Return:
        None
    """


def printpuzzle():

    """
    Prints the currently loaded puzzle to the screen.

    Args:
        None

    Return:
        None
    """

    border = "-" * 37
    print border
    for third in whole:

        i = 0
        while i < 3:
            line = ""

            # Assumes each third is assembled horizontally
            ninth = third[0]
            row = ninth[i]
            line += "| " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " "

            ninth = third[1]
            row = ninth[i]
            line += "| " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " "

            ninth = third[2]
            row = ninth[i]
            line += "| " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " |"

            line = line.replace("0", " ")

            print line
            print border

            i += 1

if __name__ == "__main__":
    printpuzzle()