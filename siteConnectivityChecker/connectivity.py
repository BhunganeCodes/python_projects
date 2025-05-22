# Import module called urllib
# Use urllib.request to get data from the url
# Write a function that takes a url
# Returns a response

import urllib.request as urllib

def main(url):
    print("Checking connectivity... ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program in Python!")
print("")
input_url = input("Enter the URL of the site you want to check!: ")

main(input_url)