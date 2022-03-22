import os

# abrindo arquivos com os ip/host
with open("Seguranca-da-Informacao-Python/exercicios_ping/hosts.txt") as f:
    dump = f.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping {}'.format(ip))
