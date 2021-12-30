import random
from sha import *
from hashlib import sha1
from memory_profiler import *

@profile()
def profiler():
    print('start')
    for i in range(100):
        print(i)
        size = random.randint(6,20)
        rdm = gen_salt(size).encode()
        hash(rdm)
        sha1(rdm).hexdigest()
    
    for i in range(10):
        print(i)
        size = random.randint(6,20)
        rdm = gen_salt(size)
        generate_password_hash(rdm)

profiler()