# https://asecuritysite.com/encryption/c_c2?m=Pay%20Eve%20%241%2C000%2C000%20-%20Bob
import sys
import os
import hashlib
import libnum
import rsaGen
import binascii
import base64
from Crypto.Util.number import long_to_bytes, inverse 
# Blinding factor
r = 3
#
def main():
	rsa_key = rsaGen.construct_key()
	rsaGen.convert_der(rsa_key)
	rsaGen.print_values()
	message = '5'
	signature = rsaGen.sign_message(message)
	val1 = (message2*pow(r, rsaGen.getPublicExponent(), rsaGen.getPublicModulus()))
	val2 = val1%rsaGen.getPublicModulus()
	print("Value sent by Heather: ", val2)
	signed_dash = pow(val2 , d , rsaGen.getPublicModulus())
	print('Heather sends Alice signature: ',signed_dash)

	result= (signed_dash * libnum.invmod(r,rsaGen.getPublicModulus()) ) %  rsaGen.getPublicModulus()

	print('Alice send signature of:',result)

	print('\n=== Check ==')
	unsigned = pow(result, rsaGen.getPublicExponent() , rsaGen.getPublicModulus())

	print('Unsigned value is:',unsigned)
	if (unsigned==rsaGen.getMessageHash()):
		print('Success. Bob has signed it')
	else:
		print('Signatures do not compute')
main()
