from random import randint      # For generating pseudo-random square roots

print("Welcome to Square Root Finder! (1.0)\n")

# Initial settings for number of points, lives and difficulty
lives = 3
points = 0
difficulty = 0

# Min and max square roots ranges (aka difficulty levels)
min_number = range(1, 10000, 1)
max_number = range(8, 10010, 1)

def reset_game():
    """
    Go back the initial game settings after player has no lives left
    """
    global lives
    global points
    global difficulty

    lives = 3
    points = 0
    difficulty = 0

    print("No lives left: You failed!.")
    print("[Restarting the game]\n")

def verify_answer(ans, good_ans):
    """
    Return True if the answer is good
    """
    if ans == good_ans:
        return True
    else:
        return False

def good_answer():
    """
    This function increases the points and difficulty after
    the player has gotten a good answer.
    """
    # Use global variables for points and difficulty
    global points
    global difficulty

    points += 1         # Increase points
    difficulty += 1     # Increase difficulty
    print("Good answer! [" + str(points) + " points]")  # Tell the user his answer is good

def bad_answer():
    """
    This function decreases the lives after the player has gotten a
    wrong answer.
    """
    global lives # Use global variable for lives
    lives -= 1   # Decrease by one life
    print("Wrong answer: Try again [" + str(lives) + " lives left]")

def one_life_left():
    """
    Return True if there is only 1 life left
    (meaning the player is about to lose)
    """
    if lives == 1:
        return True
    else:
        return False

def play():
    """
    Main loop where the player is asked to find the square root
    of multiple numbers
    """
    # Use global variables for game stats
    global lives
    global points
    global difficulty

    # Generate a new number according to difficulty level
    new_square_root = randint(min_number[difficulty], max_number[difficulty])
    perfect_square = new_square_root**2     # Square the newly generated number

    print("Find the square root of " + str(perfect_square))     # Prompt player to find square root
    while True:
        try:
            answer = input("> ")
        except KeyboardInterrupt:
            # Quit the program if CTRL + C is pressed
            exit(0)
        try:
            if verify_answer(int(answer), new_square_root): # If answer is valid
                good_answer()
                break
            else:               # If answer is invalid
                if one_life_left():
                    reset_game()    # Reset the game if all lives are lost
                    break
                else:
                    bad_answer()    # Continue if the player still have lives
        except ValueError:      # If user input is invalid (empty, or invalid caracters)
            answer = "0"
while True:
    play()
