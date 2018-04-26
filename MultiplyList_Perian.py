# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total


print(multiply([1, 2, 3, -4]))
