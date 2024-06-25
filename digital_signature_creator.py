from Crypto.Util import number
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_coprime(t):
    e = 65537  
    if gcd(e, t) == 1:
        return e
    
    for i in range(3, t, 2):  
        if gcd(i, t) == 1:
            return i

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


prime1 = number.getPrime(512)
prime2 = number.getPrime(512)
while prime1 == prime2:
    prime2 = number.getPrime(512)
n=prime1*prime2
t=(prime1-1)*(prime2-1)
e = find_coprime(t)
d = modinv(e, t)
rsa_public_key = RSA.construct((n, e))
rsa_private_key = RSA.construct((n, e, d))
public_key_pem = rsa_public_key.publickey().export_key()
message = input("Enter the original text: ").encode('utf-8')  
h = SHA256.new(message)
signature = pkcs1_15.new(rsa_private_key).sign(h)
signature_base64 = base64.b64encode(signature).decode('utf-8')
print("Digital Signature (Base64):", signature_base64)
print(public_key_pem.decode())
print(rsa_private_key.export_key())
