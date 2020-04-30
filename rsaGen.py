from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

# consisenty_check will be used to determine if the rsa_components follow RSA guidelines/rules
consistency_check = True
e = 23
d = 47
N = 143
# tuple containing values needed to construct rsa_key
rsa_components = (N, e, d)

# Construct method takes in rsa components (e, d, n) and returns rsa_key object
def construct_key():
    return RSA.construct((rsa_components))

def convert_der(rsa_key):
    f = open('public_key.pem', 'wb')
    key = rsa_key.exportKey('PEM')
    f.write(key)
    f.close()

def print_values():
    print('==Initial values ====')
    print('e=',e,'d=',d,'N=',N)
    print('\n=============')

def sign_message(message):
    f = open('public_key.pem', 'rb')
    private_key = RSA.importKey(f.read())
    f.close()
    message_hash = SHA256.new()
    message_hash.update(message.encode('utf-8'))
    print("Message Hash: ", message_hash.hexdigest())
    pkcs = PKCS1_v1_5.new(private_key)
    signature = pkcs.sign(message_hash)
    return signature
