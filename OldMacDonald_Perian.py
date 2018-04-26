#Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    fist_half = name[:3]
    second_half = name[3:]

    return fist_half.capitalize() + second_half.capitalize()





print (old_macdonald('macdonald'))

