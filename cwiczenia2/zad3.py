from gmpy2 import mpz


def opposite_point(x,y,p):
	
	y_2 = (-y) % p
	return x, y_2

x, y = mpz(2), mpz(5)
p = mpz(7)
		

x_2, y_2 = opposite_point(x,y,p)

print(f"Opposite point to P = ({x}, {y}) is P' = ({x_2}, {y_2})")
