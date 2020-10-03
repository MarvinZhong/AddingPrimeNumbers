def findprimes(n) : #statement finding primes
    primes = [] #set primes to empty list
    for i in range(2, n+1): #looping for start from 2 until input + 1
        isprime = True #set isprime's variable to boolean True
        for x in range(2, i): #looping for start from 2 until i
            if i % x == 0: #statement if i divided by x until zero
                isprime = False #make isprime's variable to boolean False
        if isprime: #statement if isprime's variable was True
            primes.append(i) #adding number primes to empty list
    primes.sort(reverse=True) #sortting primes list from max to min
    return primes #take primes data
def findadds(n, primes, start, result) : #statement finding adding be n's variable input
    if n < 0 : #statement if n smaller than 0
        return False #made as False
    elif n == 0 : #statement if n equals 0
        print(result) #print the result
        return True #made as True
    for x in range(start, len(primes)) : #looping for finding that primes numbers that equal with n
        result.append(primes[x]) #adding numbers to result list
        if findadds(n-primes[x],primes, x+1,result) : #if statement for looping if there was any number that can be equals to n
            return True #made as True
        result.remove(primes[x]) #remove number from result list if any
def findPrimesAdd() : #main statement for finding primes that adding each other would be equals n
    n = int(input()) #input n value
    findadds(n, findprimes(n), 0, []) #after input n value run findadds statement and then would run findprimes statement too
findPrimesAdd() #run main statement that named as findPrimesAdd
