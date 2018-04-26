# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x


print(unique_list([1, 1, 1, 2, 2, 3, 4, 5, 6, 4, ]))
