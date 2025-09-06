import random
options = ("rock","paper","scissor")
computer =  random.choice(options)

player = input(" enter your choice (rock,paper,scissor):").lower()


if player in options:
    if (player == computer):
        print("its a tie ")
    elif (player == "rock" and computer == "scissor")  or (player =="paper" and computer == "rock") or (player == "scissor" and computer == "paper"):
        print(f"you choose {player} and computer choose {computer}")
        print("you win")
    else:
        print("you loose")   
    
else :
    print("invalid choice please choose rock,paper or scissor :")



