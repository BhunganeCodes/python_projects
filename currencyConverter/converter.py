def main():
    print("This program converts US Dollars to Pounds Sterling")
    print("")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("The amount in Pounds is:", pounds)

convert_to_pounds = lambda dollars: dollars * 0.75

main()