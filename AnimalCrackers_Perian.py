#Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]



print(animal_crackers("Llama lava"))
