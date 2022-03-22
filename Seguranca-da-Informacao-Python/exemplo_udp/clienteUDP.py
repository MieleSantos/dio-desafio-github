import logging
import socket

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

logger.info("Cliente Socket criado com Sucesso!!")
host = "localhost"
port = 5433
message = "Olá servidor"

try:
    logger.info(f"\nCliente: {message}")
    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    logger.info(f"\nCliente: {dados}\n")
finally:
    logger.info("\nCliente: Fechando a conexão")
    s.close()
