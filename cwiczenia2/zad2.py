from gmpy2 import mpz, random_state, mpz_random,powmod
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .zad1 import generate_random_curve, generateprime
from cwiczenia1.zad4 import is_quadratic_residue
from cwiczenia1.zad5 import sqrt_modulo_p

def find_point_on_curve(A,B,p):
	rand_state = random_state(int(time.time()))

	while True:
		# x w ciele Fp
		x = mpz_random(rand_state, p)
		# oblicza y^2
		y_pow_2 = (powmod(x,mpz(3), p) + A * x + B) % p
		# sprawdza czy y^2 jest reszta kwadratowa
		if is_quadratic_residue(y_pow_2, p):
			# jezeli tak oblicza pierwiastek
			y = sqrt_modulo_p(y_pow_2, p)

			return x,y

p = generateprime()
A,B = generate_random_curve(p)
x, y = find_point_on_curve(1, 1, 7)

print(f"(x, y) = ({x}, {y})")