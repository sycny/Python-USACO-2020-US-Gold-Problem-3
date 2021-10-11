#-*-coding:utf-8-*-

import math
import sys

#find the prime
def prime(n):
    if n <= 1:
        return 0
    # for i in range(2,int(math.sqrt(n)+1)):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


#
def cow(n,m)
    L = []
    for i in range(2, n + 1):
        if prime(i):
            L.append(i)



#read data
if __name__ == "__main__":
    n = int(input("please enter the data: "))

