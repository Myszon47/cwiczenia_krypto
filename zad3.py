from gmpy2 import mpz, powmod

def exponentation(b,exp,modulo):
	b = b % modulo
	result = mpz(1)
	for i in range(exp.bit_length()):
		if exp.bit_test(i):
			result = (result * b) % modulo
		b = (b*b) % modulo
	
	return result

print(exponentation(mpz(2),mpz(6),mpz(31)))
print(powmod(mpz(2),mpz(6),mpz(31)))