# Ask user if they want to generate password or not?
# If yes, ask for password length
# If no, exit program
# Generate password
# Print the password

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like the password to be?: "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No) ")

if option == "Yes" or option == "yes":
    generate_password()
elif option == "No" or option == "no":
    print("Program ended")
    quit()
else:
    print("Invalid input! Input Yes or No")