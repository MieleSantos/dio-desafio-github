import hashlib

arquivo_1 = "a.txt"
arquivo_2 = "b.txt"

# ripemd160 algoritmo de 160 bits
hash_1 = hashlib.new("ripemd160")
hash_2 = hashlib.new("ripemd160")

hash_1.update(open(arquivo_1, "rb").read())
hash_2.update(open(arquivo_2, "rb").read())

if hash_1.digest() != hash_2.digest():
    print(f"O arquivo: {arquivo_1} é diferente do arquivo: {arquivo_2}")
    print("O hash do arquvio a.txt é: ", hash_1.hexdigest())
    print("O hash do arquvio b.txt é: ", hash_2.hexdigest())
else:
    print(f"O arquivo: {arquivo_1} é igual ao arquivo: {arquivo_2}")
    print("O hash do arquvio a.txt é: ", hash_1.hexdigest())
    print("O hash do arquvio b.txt é: ", hash_2.hexdigest())
