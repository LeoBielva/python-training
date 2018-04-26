# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False


# Or you can use , in one line; return (n1+n2) == 20 or n1==20 or n2==20


print(makes_twenty(20, 10))
