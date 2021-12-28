import io
import struct
import string
import random

# Réimplémentation de SHA1
# SHA1 est une vieille fonction cryptographique qui fut déjà attaquée maintes et maintes fois
# Elle est cependant l'une des plus simple à implémenter et qui fait un peu sens
# Je n'ai pas touché au constante bein que je n'ai pas sur trouver d'où elle venait

# Source : https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf

valeurmod = 0xffffffff

# Bitwise modulo avec 2^32
def modulo(val:int):
    return val & 0xffffffff

def functions(i:int):
    f = lambda x,y,z: x^y^z
    k = 0xca62c1d6 
    if 0 <= i <= 19:
        f = lambda x,y,z: z ^ (x & (y ^ z))
        k = 0x5a827999
    elif 20 <= i <= 39:
        f = lambda x,y,z: x^y^z
        k = 0x6ed9eba1
    elif 40 <= i <= 59:
        f = lambda x,y,z: (x&y)|(x&z)|(y&z)
        k = 0x8f1bbcdc
    return k, f

def ROL(d:int, n:int):
    return modulo((d << n) | (d >> (32 - n)))

def process(chunk:bytes, A:int, B:int, C:int, D:int, E:int):
    assert len(chunk) == 64
    w = []
    for i in range(16):
        w.append(struct.unpack(b'>I', chunk[i*4:(i+1)*4])[0])
    for i in range(16,80):
        w.append(ROL(w[i-3]^w[i-8]^w[i-14]^w[i-16], 1))
    A0 = A
    B0 = B
    C0 = C
    D0 = D
    E0 = E
    for i in range(80):
        k, f = functions(i)
        A0,B0,C0,D0,E0 = (
            modulo((w[i] + ROL(A0, 5) + f(B0, C0, D0) + E0 + k)),
            A0,
            ROL(B0, 30),
            C0,
            D0
        )
    A0 = modulo((A0 + A))
    B0 = modulo((B0 + B))
    C0 = modulo((C0 + C))
    D0 = modulo((D0 + D))
    E0 = modulo((E0 + E))
    return A0, B0, C0, D0, E0

def hash(input:bytes):
    data = io.BytesIO(input)
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    E = 0xC3D2E1F0
    taille = 0
    chunk = data.read(64)
    while len(chunk) == 64:
        # On met a jour les constantes
        A,B,C,D,E = process(chunk, A, B, C, D, E)
        # On garde la taille totale en mémoire
        taille += 64
        # On passe au suivant
        chunk = data.read(64)
    taille = taille + len(chunk)
    # On met le 1 a la fin du message (cf papier)
    chunk += b'\x80'
    # on met le bon nombre de 0 pour être congruent a 56
    chunk += b'\x00' * ((56 - (taille + 1) % 64) % 64)
    # on met la taille en 64-bit big endian
    taille_bit = taille * 8

    # > : big endian
    # Q : entier de 64 bits
    chunk += struct.pack(b'>Q', taille_bit)

    # On fait le dernier chunk : soit 64 bits soit 128
    A,B,C,D,E = process(chunk[:64], A, B, C, D, E)
    if len(chunk) == 64:
        # > : big endian
        # I : entier de 32 bits (non-signé)
        return b''.join(struct.pack(b'>I', h) for h in [A,B,C,D,E]).hex()
    A,B,C,D,E = process(chunk[64:], A, B, C, D, E)
    return b''.join(struct.pack(b'>I', h) for h in [A,B,C,D,E]).hex()

def gen_salt(length:int):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_password_hash(data:str):
    pepper = '53l3cJhxBSp465Wbne8XI97s742'
    salt = gen_salt(random.randint(10,20))
    data = salt+data+pepper
    iterations = random.randint(10000,15000)
    for i in range(iterations):
        data = hash(data.encode())
    return f'{pepper}${salt}${iterations}${data}'

def check_password_hash(pwhash:str, password:str):
    pwhash = pwhash.split('$')
    assert len(pwhash) == 4
    pepper = pwhash[0]
    salt = pwhash[1]
    iterations = int(pwhash[2])
    hashed = pwhash[3]

    password = salt+password+pepper
    for i in range(iterations):
        password = hash(password.encode())
    return password == hashed