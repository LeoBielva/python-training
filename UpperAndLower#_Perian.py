# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    d = {"upper": 0, "Lower": 0}
    for Char in s:
        if Char.isupper():
            d["upper"] += 1
        elif Char.islower():
            d["Lower"] +=1
        else:
            pass
    print("original string : ", s)
    print("No. of upper case characters : ", d["upper"])
    print("No. of lower case characters : ", d["Lower"])




print(up_low('HELLO'))
