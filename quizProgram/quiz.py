# Have a dictionary that stores questions and answers
# Have a variable that tracks score of the player
# Loop through the dict using key-value pairs
# Display question to the user and allow answer
# Feedback whether right or wrong
# Show final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital city of South Africa?",
        "answer": "Johannesburg"
    },
    "question2": {
        "question": "Which province in South Africa is the City Of Gold found?",
        "answer": "Gauteng"
    },
    "question3": {
        "question": "Which country is fully engulfed within South Africa?",
        "answer": "Lesotho"
    },
    "question4": {
        "question": "What is the Southern most province in South Africa?",
        "answer": "Limpopo"
    },
    "question5": {
        "question": "The DRC is found in which continent?",
        "answer": "Africa"
    },
    "question6": {
        "question": "What currency is used in South Africa?",
        "answer": "Rand"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("What is the answer?: ")

    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score += 1
        print("Your score is: " + str(score))
        print("")
    else:
        print("Wrong!!")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 6 questions correct!!")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")