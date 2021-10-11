# This solution to this problem can be split into two parts. 1. find all the primes with N. 2. The
# possible combinations of these primes with their powers.

# Part.1
# find the prime
def prime(n):
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

# Part.2
if __name__ == "__main__":
    #Version.2
    # The idea of dynamic programming is introduced, so it is more clear.
    # and the missing cases in the version.1 are calculated


    n,M = input("Input:N,M：").split() # input return string
    n=int(n)
    M=int(M)

    # find all the primes within N
    L = []
    for i in range(2, n + 1):
        if prime(i):
            L.append(i)

    # solve the possible largest power for all the primes
    P = []
    for i in range(len(L)):
        j = 1
        while pow(L[i], j) <= n:
            j = j + 1
        P.append(j - 1)  # while command stop before I plus one more, so minus one is the right answer
    ##

    # the PL is a list combined with P and L, we now have the basic list of primes and their powers
    PL = []
    for i in range(len(L)):
        for j in range(P[i]):
            PL.append(
                pow(L[i], j + 1))  # range command will cause one value short, it need add one to get the right answer



    m = len(PL)
    matrix = [[0 for col in range(n + 1)] for row in range(m + 1)] # build a matrix recoding the combination of steps
    matrix[0][0] = 1 # 0 change in A needs 1 step.
    PLM = PL + [M]  # add a very big prime to protect the list from out the range
    tempp = [0] * (n + 1)

    #
    for i in range(1, m + 1):
        for j in range(n - PL[i - 1] + 1):
            matrix[i][j + PL[i - 1]] = matrix[0][j] * PL[i - 1] # calculate all the possible steps combination
        if (PLM[i] % PLM[i - 1] == 0): # if the next one can not divide  the former one exactly, the next one is a new prime
            tempp = [a + b for a, b in zip(tempp, matrix[i])] # if it is the same prime, do not update the matrix[0]
        else:
            matrix[0] = [a + b + c for a, b, c in zip(matrix[0], tempp, matrix[i])]
            tempp = [0] * (n + 1)  # when moving on to the next prime, reset this temporary record

    ##print(matrix) # uncomment this code to see the matrix, which includs all possible steps.
    print(sum(matrix[0])%M) # output the answer modulo M

    # Version.1
    # The below code is the first edition code, In this code, if N<10, it works. Later on, I realize some cases
    # are missing if organized in this way. For example, if N=10, the case'5 changes+3 changes+ 2changes' is missing.
    # But this code reminds me to use matrix to recode different combination of steps.
    '''
    K = 1
    for primepower in PL:
        rest = n - primepower
        #print(rest)
       
        restL = []
        #add one step to verify whether the primepower is the prime or the power of primes
        ##
        for primes in L:
            if (primepower%primes==0)&(primepower/primes==1):
                for primes in L:
                     if primes > primepower:
                            if rest >= primes:
                               restL.append(primes)
                    
            elif (primepower%primes==0)&(primepower/primes!=1):
                primepowerPL = primes
                for primes in L:
                     if primes > primepowerPL:
                            if rest >= primes:
                               restL.append(primes)
        K = K + sum([i * primepower for i in restL]) + primepower
        print(K)
    
    '''







