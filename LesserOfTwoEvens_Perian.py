# Write a function that returns the lesser of two given numbers if both numbers are even, but return the greater if one ot both numbers are odd

def lesser(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if  a < b:
            # Or you can just do, return min(a,b)
            result = a

        else:
            result = b
    else:
        # Or you can just do, return max(a,b)
        if a > b:
            result = a
        else:
            result = b

    return result


print(lesser(7,5))

