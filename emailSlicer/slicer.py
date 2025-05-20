# Collect email from user
# Slice or split the email using @, save first part as username. Second part will be saved as domain
# Split the domain using "."

def main():
    print("Welcome to the Email Slicer")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()

