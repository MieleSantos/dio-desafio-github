## ICMP

- ICMP(Internt COntrl Message Protocolç), é um protocolo integrante do Protocolo IP utilizado para fornecer relatórios de erros á fonte original

## Ping
- É uma ferramenta que usa o protocolo icmp para testa a conectividade entre nós e para isso, envia pacotes para os equipamentos de destino e escuto a resposta
- O ping é comtemplado pelo princípio  da [Disponibilidade](principios.md)

- Exemplos usando ping
    - [Exemplos 1](exercicios_ping/pingsimples.py)<br>
    - [Exemplos 2](exercicios_ping/pingmultiplo.py)<br>

## TCP

- O TCP(Transmission Control) ou Protocolo de Controle de transmissão é um dos protocolos de comunicação, que dão suporte a rede global de internet, verificando se os dados são enviados na sequência correta e sem error

- Esse protocolo contempla o pricípio da [Integridade](principios.md)

- Exemplo usando TCP
    - [Exemplo](exercicios_ping/clientetcp.py)

## UDP

- O UDP (User Datagram Protocol) ou Protocolo de Datagrama de usuário é um protocolo simples da coada de transporte que permite que a aplicação envie um datagrama dentro num pacote IPV4 ou IPV6 a um destimo, pórem sem qualquer tipo de garantia que o pacote chegue corretamente.

- Este protocolo contempla o princípio da [Disponibilidade](principios.md)

- Exemplo usando UDP(Criando um client/Servidor para enviar mensagem)<br>
    Execute o servidor e depois o client
    - [Servidor](exemplo_udp/server_udp.py)
    - [Client](exemplo_udp/client_udp.py)

## Biblioteca Random

- É usada para gerar senhas randomizando letras e números e a cada execução do programa, novas senhas são geradas

- Essa biblioteca contempla os princípios da [Autenticação](ping.md) e da [Confidencialidade](ping.md)

## Hash

- É como se um identificador único gerado através de um algoritmo que vai analisar
byte a byte de determinado dado para gerar de forma única, um determinado código que só aquele arquivo terá. Se neste mesmo arquivo um único bit for alterado o hash gerado será diferente.
- O Hash contempla o princípio da [Integridade](ping.md)

## ipaddress

- Esta biblioteca tem a capaciade de criar, manipular endereços IP do tipo IPv4, Ipv6 e até redes inteiras