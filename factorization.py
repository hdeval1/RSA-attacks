# Code adapted from https://asecuritysite.com/encryption/rsa12_2
from Crypto.Util.number import long_to_bytes
import libnum
import sys
import timeit
import math

# Implementation of Factorization Attack on RSA 
# Heather DeVal, Jordan Fok, Hannah Russell 
# CMSC 443 Final Project

N=36391
c1=35338

def print_values():
    print("Welcome to the Factorization Attack on RSA!")
    print("The key values used in the RSA algorithm will be printed below. Note: I only have ciphertext, and one prime number value - N")
    print("The ciphertext is: ", c1)
    print("The value of one prime (N) is ", N)
    print("**************ATTACK BEGINNING*****************")
    print()
    print()

def factorTime():
    print ("Finding factors for",N)
    rtn=getfactor(N)
    print ("Factors are: ",rtn)
    p = rtn[0]
    q = rtn[1]    
    n = p*q
    print("The product of the two primes is n: ", n)
    PHI=(p-1)*(q-1)
    print("Using the two primes and Euler's law, phi is determined: ", PHI)
    e=65537
    d=(libnum.invmod(e, PHI))
    print("The private exponent d is determined using phi and the public exponent e (guessing 65537  - most commonly used)")
    print("The value of d is: ", d)
    print ("\n=== Attempting Decryption....... ===")
    res1=pow(c1,d,n)
    print ("The decrypted ciphertext is: %s" % long_to_bytes(res1))

def timing():
    print("Time to execute attack: " + str(timeit.timeit(factorTime, number=1)) +" seconds.")

def getfactor(y):
        i=0
        while True:
                val = y + i*i
#               print i,val
                sq = int(math.sqrt(val))
                if (sq*sq == int(val)):
                        print ("Factors: (",sq,"+",i,"),(",sq,"-",i,")")
                        return(sq-i,sq+i)
                i=i+1
                if (i==10000): return("Cannot find")
        return "Cannot find"

def main():
    value = N
    print_values()
    factorTime()
    timing()


main()