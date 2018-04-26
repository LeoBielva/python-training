# Write a Python function to check whether a string is pangram or not.

def palindrome(s):
    return s == s[::-1]


print(palindrome('madam'))
