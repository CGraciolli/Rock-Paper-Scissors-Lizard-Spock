from instances import dictionary
from random import randrange, choice

def display_game():
    print("\nRock, Paper, Scissors, Lizard, Spock")

def get_user_pick():
    print("\n1.Rock\n2.Paper\n3.Scissors\n4.Lizard\n5.Spock\n")
    pick = 0
    while pick not in list(dictionary.keys()):
        pick = input("Please, type a number between 1 and 5: ")
    return dictionary[pick]

def get_random_pick():
    pick = randrange(1, len(dictionary)+1)
    return dictionary[str(pick)]

def get_winner(pick1, pick2):
    if pick1 > pick2:
        return "you"
    elif pick2 > pick1:
        return "the computer"

def display_tie():
    print(f"There has been a tie.")

def display_victory(winner):
    print(f"{winner.capitalize()} won! \n")

def ask_to_play_again():
    insults = ["Your father was a hamster and your mother smelled of elderberries", "A most notable coward, an infinite and endless liar, an hourly promise breaker, the owner of no one good quality.",
    "I am sick when I do look on thee", "I fart in your general direction"]
    answer = 0
    while answer != "N" and answer != "Y":
        answer = input("Do you want to play again? (Y/N)").upper()
    if answer == "N":
        insult = choice(insults)
        print(insult)
    return answer == "Y"

def display_player_move(pick):
    print(f"\nYou chose {pick}. {pick.emoji}")

def display_computer_move(pick):
    print(f"The computer chose {pick}. {pick.emoji} \n")

def display_count(you, pc):
    print(f"You {you} x {pc} Computer\n")

def run_game():
    """
    starts the game
    """
    go_on = True
    you = 0
    computer = 0
    display_game()
    while go_on:
        user_pick = get_user_pick()
        comp_pick = get_random_pick()
        display_player_move(user_pick)
        display_computer_move(comp_pick)
        winner = get_winner(user_pick, comp_pick)
        if winner == "you":
            you += 1
        elif winner == "the computer":
            computer += 1
        if winner == None:
            display_tie()
        else:
            display_victory(winner)
        display_count(you, computer)
        go_on = ask_to_play_again()

if __name__ == "__main__":
    run_game()

