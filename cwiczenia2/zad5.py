from gmpy2 import mpz
from zad4 import eliptic_sum

def n_multiply_P(n, x1, y1, p, A):
	x, y = x1, y1
	while n > mpz(0):
		x, y = eliptic_sum(x1, y1, x, y, p, A)
		n -= mpz(1)
	
	return x, y

print(n_multiply_P(mpz(5), mpz(0), mpz(1), mpz(7), mpz(1)))