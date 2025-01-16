import random
def get_choices():
    player_choice = input("enter a choice")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer" : computer_choice}

    return choices

def check_win(player, computer):
    print(f"you chose {player} computer chose {computer}") # f is for concatenating
    if player == computer:
        return "it's a tie"
    elif computer == "rock":
        if player == "paper":
            return "player wins"
        else : 
            return "player loses"
    elif computer == "paper":
        if player == "scissors":
            return "player wins"
        else : 
            return "player loses"
    elif computer == "scissors":
        if player == "rock":
            return "player wins"
        else : 
            return "player loses"
    

print(check_win(get_choices()["player"], get_choices()["computer"]))






