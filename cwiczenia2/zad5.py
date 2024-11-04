from gmpy2 import mpz
from zad4 import eliptic_sum

def n_multiply_P(n, x1, y1, p, A):

	Qx, Qy = None, None
	x, y = x1, y1

	for i in range(n.bit_length()):
		if n.bit_test(i):
			if Qx is None and Qy is None:
				Qx, Qy = x, y
			else:
				Qx, Qy = eliptic_sum(Qx, Qy, x, y, p, A)
		
		x, y = eliptic_sum(x, y, x, y, p, A)

	
	return Qx, Qy

print(n_multiply_P(mpz(6), mpz(0), mpz(1), mpz(7), mpz(1)))