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



#def greeting():
#    return "HI"

#print(greeting())


#choices = get_choices()
#print(choices)

#distcionary is a key value pair where the value can be a variable
#dict = {"name": "beau", "color": "blue"}

 #Librarires are a set of useful functions without writing additional functions 
#Lists are used to store multiple itesm in a single variable

#food = ["pizza", "carrots", "eggs"]
#dinner = random.choice(food) #to choose a random item from teh list

# combining strings usin fstring method 
#age = 25 
# print (f"Jim is {age} years old")



