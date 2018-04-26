#Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    if n in range(89, 111):
        return True
    elif n in range(189, 211):
        return True
    else:
        return False



print(almost_there(200))






def almost_there2(x):
    return (abs(100-x) <= 10) or (abs(200-x) <= 10)               #abs(num)returns the absolute value of a number




print(almost_there2(209))