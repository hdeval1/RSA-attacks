from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
# consisenty_check will be used to determine if the rsa_components follow RSA guidelines/rules
consistency_check = True
e = 65537
prime1= 837617279 
prime2= 825132317 
#d = 15116834464032299802948943494672044499122828099564500659296561669886791811312806805869815404149447214369635112393521664772355117942911383376888182528302846884976855464649056449418159728717267320241159017179044587944663545847668273
d = 649140859856355089
N = prime1*prime2
# tuple containing values needed to construct rsa_key
rsa_components = (N, e, d)
# Important Variables to pass through classe
mhash = MD5.new()
priv_key = None
# Construct method takes in rsa components (e, d, n) and returns rsa_key object
def construct_key():
    return RSA.construct((rsa_components))

def getPublicExponent():
    return e

def getPublicModulus():
    return N
def convert_der(rsa_key):
    f = open('private_key.pem', 'wb')
    key = rsa_key.exportKey('PEM')
    f.write(key)
    f.close()

def getPrivateKey():
    return priv_key

def setMessageHash(message):
    mhash.update(message.encode("utf8"))
 #   print("Message Hash:", mhash.digest())

def getMessageHash():
    return mhash

def sign_message(message):
    f = open('private_key.pem', 'rb')
    priv_key = RSA.importKey(f.read())
    f.close()
    setMessageHash(message)
    pkcs = PKCS1_v1_5.new(priv_key)
    print("PKCS: ", pkcs)
    signature = pkcs.sign(mhash)
    if (pkcs.verify(mhash, signature)):
        print("The signature: \n" + str(signature) + "\nWas verified for the message hash: \n" +str(mhash.hexdigest()))
        return signature
    else:
        return null

def print_values():
    print('==Initial values ====')
    print('e=',e,'\nd=',d,'\nN=',N)
    print('\n=============')
