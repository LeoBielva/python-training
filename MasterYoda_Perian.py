#Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    wordlist = text.split()                                 #splits string into word strings
    reverse_wordlist = wordlist[::-1]                       #create a new variable with variable wordlist reversed[::-1}
    return ' '.join(reverse_wordlist)                       #''(string value) if theres in between it will usa that in between to separate words, and .join transforms list into string




print (master_yoda('I am home'))
