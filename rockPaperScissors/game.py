import random

exit = False
user_score = 0
computer_score = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input.lower() == "exit":
        print("Goodbye! Game ended")
        exit = True
        print(f"Your score is {user_score} points! and the computer scored {computer_score} points!")


    elif user_input.lower() == "rock":
        if computer_input == "rock":
            print("You chose rock")
            print("Computer chose rock")
            print("It's a tie!")
        elif computer_input == "paper":
            print("You chose rock")
            print("Computer chose paper")
            print("You Lose!")
            computer_score += 1
        elif computer_input == "scissor":
            print("You chose paper")
            print("Computer chose scissors")
            print("You win!")
            user_score += 1

    elif user_input.lower() == "paper":
        if computer_input == "rock":
            print("You chose paper")
            print("Computer chose rock")
            print("You win!")
            user_score += 1
        elif computer_input == "paper":
            print("You chose paper")
            print("Computer chose paper")
            print("It's a tie!")
        elif computer_input == "scissor":
            print("You chose paper")
            print("Computer chose scissors")
            print("You lose!")
            computer_score += 1

    elif user_input.lower() == "scissors":
        if computer_input == "rock":
            print("You chose scissors")
            print("Computer chose rock")
            print("You lose!")
            computer_score += 1
        elif computer_input == "paper":
            print("You chose scissors")
            print("Computer chose paper")
            print("You win!")
            user_score += 1
        elif computer_input == "scissor":
            print("You chose scissors")
            print("Computer chose scissors")
            print("You lose!")
    
    elif user_input != "rock" or user_input != "rock" or user_input != "scissors" or user_score != "exit":
        print("Invalid input!")