# https://asecuritysite.com/encryption/c_c2?m=Pay%20Eve%20%241%2C000%2C000%20-%20Bob
import sys
import os
import hashlib
import libnum

e=79
d=1019
N=3337
r=21
Message='Pay Eve $1 million'

print('==Initial values ====')
print('e=',e,'d=',d,'N=',N)
print('message=',Message,'r=',r)
print('\n=============')

array = os.urandom(1 << 20)
md5 = hashlib.md5()
md5.update(array)
digest = md5.hexdigest()
M = int(digest, 16) % N

print('MD5 hash (mod N): ',M)

signed=pow(M,d , N)
print('Signed:\t',signed)

val_sent_by_eve = (M*pow(r,e, N))%N

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