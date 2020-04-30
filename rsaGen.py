from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# consisenty_check will be used to determine if the rsa_components follow RSA guidelines/rules
consistency_check = True
e = 79
d = 1019
N = 3337
# tuple containing values needed to construct rsa_key
rsa_components = (N, e, d)

# Construct method takes in rsa components (e, d, n) and returns rsa_key object
def construct_key():
    rsa_key = RSA.construct(rsa_components, consistency_check)
    return rsa_key

def convert_der(rsa_key):
    f = open('private_key.der', 'wb')
    f.write(rsa_key.export_key('DER', '1234'))
    f.close()

def print_values():
    print('==Initial values ====')
    print('e=',e,'d=',d,'N=',N)
    print('\n=============')

def sign_message(message):
    private_key = RSA.import_key(open('private_key.der', '1234').read())
    message_hash = SHA256.new(message)
    print("Message Hash: ", message_hash)
    signature = pkcs1_15.new(private_key).sign(message_hash)
    return signature
