# Code adapted from https://asecuritysite.com/encryption/c_c2
import sys
import os
import hashlib
import libnum
import timeit

# Implementation of the Blinding Attack on RSA 
# Heather DeVal, Jordan Fok, Hannah Russell 
# CMSC 443 Final Project

e=79
d=1019
N=3337
r=21


def getMessage():
    message= input("What is your message? \n")
    return message

def print_values(message):
    print('== Welcome to the RSA Blinding Attack! ====')
    print('Public Key Exponent (e) =',e)
    print('Private Key Exponent (d) = ',d)
    print('Multiplication of two primes (n) =',N)
    print('Message to send =',message)
    print('Random blinding factor (r) =',r)
    print('\n=============')

def blindingAttack():
    array = os.urandom(1 << 20)
    md5 = hashlib.md5()
    md5.update(array)
    digest = md5.hexdigest()
    M = int(digest, 16) % N
    print('The MD5 hash for your message:', digest)
    print('The value of MD5 hash mod n', M)
    signed=pow(M,d , N)
    print('The message is signed with the signature:\t',signed)
    value_sent = (M*pow(r,e, N))%N
    signed_value = pow(value_sent , d , N)
    print('You send the hacker your public signature: ',signed_value)
    result= (signed_value * libnum.invmod(r,N) ) %  N
    print('The hacker sends back your private signature of:',result)
    print('\n=== Let\'s Check If It Worked!==')
    unsigned = pow(result,e , N)
    print('The value of the unsigned message is:',unsigned)
    checkValue(unsigned, M)

def checkValue(unsigned, M):
    if (unsigned==M):
        print('*******YOU HAVE BEEN HACKED! THE MESSAGE HAS YOUR PRIVATE SIGNATURE ON IT**********')
    else:
        print('Lucky you! Something did not work out right. It does not appear you sent the other message.')

def timing():
    print("Time to execute attack: " + str(timeit.timeit(blindingAttack, number=1)) +" seconds.")

def main():
    message = getMessage()
    print_values(message)
    blindingAttack()
    timing()
main()