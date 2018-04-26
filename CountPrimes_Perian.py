#Write a function that returns the number of prime numbers that exist up to and including a given number 0&1 are not prime

def count_prime(num):
    #check for 0 in 1 input
    if num < 2:
        return 0
    ###############
    #2 or greater
    ###############

    #Store our prime numbers
    primes = [2]
    #counter going up to the input num
    x = 3
    #x is going through every number up to input num
    while x <= num:
        #check if x is prime
        for y in range(3,x,2):
            if x%y ==0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)




print(count_prime(100))