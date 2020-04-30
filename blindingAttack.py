# https://asecuritysite.com/encryption/c_c2?m=Pay%20Eve%20%241%2C000%2C000%20-%20Bob
import sys
import os
import hashlib
import libnum
import rsaGen


def main():
	rsa_key = rsaGen.construct_key()
	rsaGen.convert_der(rsa_key)
	rsaGen.print_values()
	message = 'Hi Bob'
	signature = rsaGen.sign_message(message)
	print('Signed:\t',signature)

main()
val_sent_by_eve = (M*pow(r,e, N))%N
print("value sent by eve: ", val_sent_by_eve)
signed_dash = pow(val_sent_by_eve , d , N)

print('Bob sends Eve signature: ',signed_dash)

result= (signed_dash * libnum.invmod(r,N) ) %  N

print('Eve send signature of:',result)

print('\n=== Check ==')
unsigned = pow(result,e , N)

print('Unsigned value is:',unsigned)
if (unsigned==M):
	print('Success. Bob has signed it')
else:
	print('Signatures do not compute')