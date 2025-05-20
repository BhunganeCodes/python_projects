# Define a function that takes a list and target parameter
# Multiple variables: middle, start, end and steps
# Recursion or While loop. (recursion makes more sense)
# Increase steps each time a split is done
# Conditions: ternary operators to track target position

def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print("Steps", steps, ":", str(list[start:end+1]))

        steps += 1
        middle = (start + end) // 2

        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return - 1

list = [1,2,3,4,5,6,7,8,9]
target = 7

binary_search(list, target)