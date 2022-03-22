import logging
import socket

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

host = "localhost"
port = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
logger.info("\nSocket criando com sucesso")

s.bind((host, port))
message = "\nServidor: Olá"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        logger.info("\nServidor enviando mensagem")

        s.sendto((dados + message.encode()), end)
