import random
import string

def senha_aleatoria():
	chars = string.ascii_letters + string.digits
	senha = ''.join((random.choice(chars) for i in range(12)))

	return senha