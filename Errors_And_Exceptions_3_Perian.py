#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            i = int(input("Please enter a number: "))
        except:
            print("Input at intiger: null")
            print("An error ocurred, Please try again")
        else:
            print("Input at intiger: ", i)
            print("Thank you, your number squared is: ", i**2)
            break

if __name__ == '__main__':
    ask()