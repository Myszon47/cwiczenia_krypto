from gmpy2 import mpz, powmod, invert

def eliptic_sum(x1, y1, x2, y2, p, A):
	if x1 == float('inf'):
		return x2, y2
	elif x2 == float('inf'):
		return x1, y1
	elif x1 != x2:
		lam = ((y2- y1) * invert(x2-x1, p)) % p
		x3 = (powmod(lam, mpz(2), p) - x1 - x2) % p
		y3 = (lam * (x1-x3) - y1) % p
		return x3, y3
	elif y1 == y2:
		lam = ((mpz(3) * (powmod(x1,mpz(2), p)) + A) * invert(2*y1, p)) % p
		x3 = (powmod(lam, mpz(2), p) - mpz(2) * x1) % p
		y3 = (lam * (x1 - x3) - y1) % p
		return x3, y3
	elif y1 == ((-y2) % p):
		return float('inf'), float('inf')
 	

print(eliptic_sum(mpz(0),mpz(1),mpz(0),mpz(6),mpz(7),mpz(1)))