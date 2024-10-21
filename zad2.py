from gmpy2 import mpz, invert, f_div


def eukliedes(a,b):
	if a == 0:
		return b, mpz(0), mpz(1)
	NWD, x1, y1 = eukliedes(b%a, a)
	x = y1 - f_div(b,a) * x1
	y = x1
	return NWD, x, y

def inverse(b,n):
	NWD, x, y = eukliedes(b,n)
	if NWD != 1:
		print("nie sa wzglednie pierwsze")
	else:
		return x % n

print(inverse(mpz(17),mpz(7)))
print(invert(1001,5))