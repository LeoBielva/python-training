# def with *args
def myfunc(*args):
    mylist = [a for a in args if a%2 == 0]
    return mylist


print(myfunc(1, 2, 3, 4, 5, 6))