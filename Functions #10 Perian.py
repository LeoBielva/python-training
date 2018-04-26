def myfunc(strg):
    nstrg=''
    for i in range(len(strg)):
        if i%2 ==0:
            nstrg += strg[i].lower()
        else:
            nstrg += strg[i].upper()
    return nstrg

print(myfunc('leonardo'))
