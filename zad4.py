from zad3 import exponentation
from gmpy2 import mpz, f_div

def is_quadratic_residue(b,p):
	exponent = f_div((p-mpz(1)), mpz(2))
	result = exponentation(b, exponent, p)

	return result == mpz(1)

print(is_quadratic_residue(mpz(5),mpz(11)))