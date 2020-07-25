def prime_numbers(x):
    count=0
    if (x>1):
        for i in range(2,x+1):
            if(x % i) == 0:
                count=count+1 
        if count==1:
            return True
        else:
            return False
    else:
        return False

    
def count_primes(num):
    counter = 0
    for i in range(2, num + 1):
        if prime_numbers(i):
            counter += 1
    print("There are",counter,"prime numbers between 0 and",num)
