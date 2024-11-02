from gmpy2 import mpz, random_state, mpz_random, next_prime, powmod
import time

def generateprime():
    rand_state = random_state(int(time.time()))
    p = mpz_random(rand_state, mpz(2)**mpz(300))
    p = next_prime(p)
    while p % mpz(4) != mpz(3):
        p = next_prime(p)
    return p

def generate_random_curve(p):
    rand_state = random_state(int(time.time()))
    
    while True:
        A = mpz_random(rand_state, p)
        B = mpz_random(rand_state, p)

        # sprawdza warunek delty
        delta = (mpz(4) * powmod(A, mpz(3), p) + mpz(27) * powmod(B, mpz(2), p)) % p

        if delta != mpz(0):
            return A, B


p = generateprime()  
A, B = generate_random_curve(p)

print(f"A = {A}, B = {B}")
