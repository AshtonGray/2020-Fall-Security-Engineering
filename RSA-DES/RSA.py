
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    origz = z
    set1 = [1,0]
    set2 = [0,1]
    xy = [0,0]
    while e%z != 0:
        mod = e % z
        quot = e // z
        xy[0] = set1[0] - quot*set2[0]
        xy[1] = set1[1] - quot*set2[1]
        # Swap variables and sets
        set1 = set2.copy()
        set2 = xy.copy()
        e = z
        z = mod

    # Negative d Protection
    if xy[0] < 0:
        while xy[0] < 0:
            xy[0] += origz
    d = xy[0]
    return d

def is_prime (num):
    if num > 1:
      
        # Iterate from 2 to n / 2  
        for i in range(2, num//2):
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    n = p*q
    z = (p-1) * (q-1)
    e = random.randint(1, n - 1)
    while gcd(e, z) != 1:
        e = random.randint(1, n-1)

    d = get_d(e, z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    encoded = ord(plaintext)
    e = pk[0]
    n = pk[1]
    cipher = pow(encoded, e, n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext

    d = pk[0]
    n = pk[1]
    plain = pow(ciphertext, d, n)
    plain = chr(plain)
    return ''.join(plain)

