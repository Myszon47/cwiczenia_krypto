from gmpy2 import mpz, random_state, mpz_random
import time
import random

def random_number_Zn(n,k):

        seed = int(time.time())
        state = random_state(seed)
        random_number = mpz_random(state, 2**k)
        result = random_number % n

        return result


print(random_number_Zn(mpz(12),mpz(24)))

def random_numb_Zn(k):
        random.seed(int(time.time()))

        bits = '1' + ''.join(str(random.randint(0,1)) for bit in range(k-1))
        number = mpz(bits, 2)
        result = number 

        return result

print(random_numb_Zn(1024))