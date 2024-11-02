import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .zad3 import exponentation
from gmpy2 import mpz, f_div

def sqrt_modulo_p(b,p):
	exp = f_div((p+mpz(1)), mpz(4))
	return exponentation(b,exp,p)


print(sqrt_modulo_p(mpz(5),mpz(11)))