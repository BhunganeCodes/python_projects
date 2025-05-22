# Have a python dictionary with key-value pair that represents word and definition
# Collect input from the user, input is the word (key)
# Check if the word is in the dictionary and print dictionary

def main():
    word_dictionary = {
        "hello": "a way of greeting",
        "eyes": "organ for seeing",
        "food": "basic form of energy ingested orally"
    }


    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()