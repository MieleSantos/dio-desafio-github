import logging
import socket
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    try:
        # criando socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        logger.info("A conexão falhou!!!")
        logger.error(f"ERRO: {e}")
        sys.exit()

    print("Socket criado com sucesso")

    host_alvo = input("Digite o host ou ip a ser conectado: ")
    porta_alvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        logger.info(
            "Cliente TCp conectado com Sucesso no host"
            + f": {host_alvo} na porta: {porta_alvo}"
        )
        # finalizando a conexao depois de 2 segundos
        s.shutdown(2)
    except socket.error as e:
        logger.info("A conexão falhou")
        logger.error(f"Error: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
