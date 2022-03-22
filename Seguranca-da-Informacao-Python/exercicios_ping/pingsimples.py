import os

print("#" * 60)
ip_ou_host = input("Digite o ip ou host para ser verificado: ")

# fazendo o ping para o ip ou host
os.system('ping {}'.format(ip_ou_host))
