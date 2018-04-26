#Given a string, return a string where for every character in the original there are three characters\

def paper_doll(text):
    result = ''                         #result setup as an empty string
    for char in text:
        result += char*3
    return result


print(paper_doll('yousuck'))