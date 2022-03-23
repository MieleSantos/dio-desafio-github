import random
import string

# recomendação de senha com 16 caracteres
tamanho = 16

# letters envolve letras maiusculas e minusculas
chars = string.ascii_letters + string.digits + "!@#$%&*()-_=+/.,;:|/?^~[{]}"
rnd = random.SystemRandom()  # os.urandom gera numeros aleatorios

senha = "".join(rnd.choice(chars) for i in range(tamanho))
print(senha)
