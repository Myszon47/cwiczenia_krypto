from zad3 import exponentation
from gmpy2 import mpz, random_state, mpz_random, c_div, is_prime

def miller_rabin(n, k=5):

    if n <= mpz(1):
        return False
    if n <= mpz(3):
        return True
    if n % mpz(2) == mpz(0):
        return False

    r, d = mpz(0), n - mpz(1)
    while d % mpz(2) == mpz(0):
        d = c_div(d,mpz(2))
        r += mpz(1)

    def is_composite(a):
        if exponentation(a, d, n) == mpz(1):
            return False
        for i in range(r):
            if exponentation(a, mpz(2)**i * d, n) == n - mpz(1):
                return False
        return True
    
    rand_state = random_state()

    for _ in range(k):
        a = mpz_random(rand_state, n-mpz(2)) + mpz(2)
        if is_composite(a):
            return False

    return True

print(miller_rabin(mpz(104549)))
print(is_prime(mpz(104549)))


