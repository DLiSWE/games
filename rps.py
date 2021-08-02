import random


choices = ['rock', 'paper', 'scissor']
comp_choice = random.choice(choices)
counter = 0
scoreboard = {'W': 0, 'L': 0, 'T': 0}
results = ['Victory', 'Defeat', 'Tie']
compare = [" "]

def banner_text(text, screen_width = 80):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)

banner_text("*")
banner_text("Rules for the game:")
banner_text("1. Choose your choice between rock, paper or scissor(s).")
banner_text("2. The scoreboard will update after every game.")
banner_text("3. After each game, you will be prompted to continue or not. (y/n)")
banner_text("4. After the 10th game, the program will close.")
banner_text("*")
user_name = input("Enter your name:")
banner_text(user_name)
user_input = input("Please choose the following: Rock, Paper, or Scissors: ")

def rock_p_scissor(user_input, comp_choice):
    """
    This function compares the user input to the random computer choice and spits
    the result out, as well as update the scoreboard.
    :param user_input:
    :param comp_choice:
    :return:
    """
    if user_input.lower() == comp_choice:
        compare = results[2]
        score_update(scoreboard, compare)
        banner_text("*")
        banner_text("Tie! We both chose {0}".format(user_input))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    elif user_input.lower() == 'rock' and comp_choice == 'paper':
        compare = results[1]
        score_update(scoreboard, compare)
        print("You lost! you chose {0} and I chose {1}".format(user_input, comp_choice))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    elif user_input.lower() == 'rock' and comp_choice == 'scissor':
        compare = results[0]
        score_update(scoreboard, compare)
        print("You won! you chose {0} and I chose {1}".format(user_input, comp_choice))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    elif user_input.lower() == 'paper' and comp_choice == 'scissor':
        compare = results[1]
        score_update(scoreboard, compare)
        print("You lost! you chose {0} and I chose {1}".format(user_input, comp_choice))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    elif user_input.lower() == 'paper' and comp_choice == 'rock':
        compare = results[0]
        score_update(scoreboard, compare)
        print("You won! you chose {0} and I chose {1}".format(user_input, comp_choice))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    elif user_input.lower() == 'scissor' or user_input.lower() == 'scissors' and comp_choice == 'rock':
        compare = results[1]
        score_update(scoreboard, compare)
        print("You lost! you chose {0} and I chose {1}".format(user_input, comp_choice))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    elif user_input.lower() == 'scissor' or user_input.lower() == 'scissors' and comp_choice == 'paper':
        compare = results[0]
        score_update(scoreboard, compare)
        print("You won! you chose {0} and I chose {1}".format(user_input, comp_choice))
        banner_text("*")
        print(scoreboard)
        banner_text("*")
    else:
        print("Your input was not valid. Please try again")


def score_update(scoreboard, compare):
    """
    This function adds 1 to the scoreboard.
    :param scoreboard:
    :param compare:
    :return:
    """
    if compare == 'Victory':
        scoreboard['W'] += 1
    elif compare == 'Defeat':
        scoreboard['L'] += 1
    elif compare == 'Tie':
        scoreboard['T'] += 1

def post_game():
    '''TODO: Create User input that asks for how many games they want to play. Make this a parameter in
    function and change in function. 
    '''
    while counter < 50:
        #This function limits the amount of tries this game provides.
        counter += 1
        comp_choice = random.choice(choices)
        rock_p_scissor(user_input, comp_choice)
        again = input("Again?(y/n)")
        if again.lower() == "y" or again.lower() == "yes":
            comp_choice = random.choice(choices)
            banner_text(" ")
            user_input = input('What is your pick?')
            banner_text(" ")
        elif again.lower() == "n" or again.lower() == "no":
            print(scoreboard)
            if scoreboard['W'] > scoreboard['L']:
                banner_text("*")
                banner_text(" ")
                banner_text("YOU WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                banner_text(" ")
                banner_text("*")
            elif scoreboard['W'] > scoreboard['L'] * 3:
                banner_text("*")
                banner_text(" ")
                banner_text("DECISIVE VICTORY!!!!")
                banner_text(" ")
                banner_text("*")
            elif scoreboard['L'] > scoreboard['W']:
                banner_text("*")
                banner_text(" ")
                banner_text("CLOSE LOSS! Try Again!")
                banner_text(" ")
                banner_text("*")
            elif scoreboard['L'] > scoreboard['W'] * 3:
                banner_text("*")
                banner_text(" ")
                banner_text('Huge Loss. Better luck next time.')
                banner_text(" ")
                banner_text("*")
            else:
                banner_text('Tie I guess?')
            break
        else:
            again
            break
