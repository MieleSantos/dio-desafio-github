import hashlib

arquivo_1 = "a.txt"
arquivo_2 = "b.txt"

# ripemd160 algoritmo de 160 bits
hash_1 = hashlib.new("ripemd160")

hash_1.update(open(arquivo_1, "rb")).read()
