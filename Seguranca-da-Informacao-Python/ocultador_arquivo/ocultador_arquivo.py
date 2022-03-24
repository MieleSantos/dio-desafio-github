import ctypes

pasta = input("Digite a caminho da pasta aser ocultada ex (C:/pasta): ")
atributo_ocultar = 0x02
if pasta:
    retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

else:
    retorno = ctypes.windll.kernel32.SetFileAttributesW(
        "ocultar.txt", atributo_ocultar
    )

if retorno:
    print("Arquivo foi ocultado")
else:
    print("O arquivo nao foi ocultado")
