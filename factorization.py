# Code adapted from https://asecuritysite.com/encryption/rsa12_2
from Crypto.Util.number import long_to_bytes
import libnum
import sys
import timeit

# Implementation of Factorization Attack on RSA 
# Heather DeVal, Jordan Fok, Hannah Russell 
# CMSC 443 Final Project


p=954354002755510667
q=801297755486859913
c=11287380433570645142834656528478983

def print_values():
    print("Welcome to the Factorization Attack on RSA!")
    print("The key values used in the RSA algorithm will be printed below. Note: I only have ciphertext, and two prime number values")
    print("The ciphertext is: ", c)
    print("The value of one prime (q) is ", q)
    print("The value of another prime (p) is ", p)
    print("**************ATTACK BEGINNING*****************")
    print()
    print()

def factorTime():
    n = p*q
    print("The product of the two primes is n: ", n)
    PHI=(p-1)*(q-1)
    print("Using the two primes and Euler's law, phi is determined: ", PHI)
    e=65537
    d=(libnum.invmod(e, PHI))
    print("The private exponent d is determined using phi and the public exponent e (guessing 65537  - most commonly used)")
    print("The value of d is: ", d)
    print ("\n=== Attempting Decryption....... ===")
    res=pow(c,d, n)
    print ("The decrypted ciphertext is: %s" % ((long_to_bytes(res))))

def timing():
    print("Time to execute attack: " + str(timeit.timeit(factorTime, number=1)) +" seconds.")

def main():
    print_values()
    factorTime()
    timing()

main()