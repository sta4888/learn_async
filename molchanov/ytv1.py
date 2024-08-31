import socket

# socket.AF_INET - это IP протокол 4 мерсии
# socket.SOCK_STREAM - говорит о том, что речь пойдет о протоколе TCP
# в Ubuntu 3 мин на освобождение порта
# server_socket имеет метод accept - который принимает входящее подключение (он читает данные из входящего буфера,
# и если на вход пришло что либо [какое то подключение] то он возвращает нам кортеж {у этого кортежа 2 элемента} сокет клиента и адрес)


# для того, чтоб протестировать этот код, необходимо скачать и установить nmap в нем есть netcat и после запуска .py
# скрипта в соседнем окне терминала нам необходимо прописать команду `ncat -C localhost 5001`


# можно писать асинхронный код с помощью callback asyncio и ч помощью генераторов и корутин

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()

while True:
    print('accept')
    client_socket, client_address = server_socket.accept()
    print(f'Connected by: {client_address}')

    while True:
        print('recv')
        request = client_socket.recv(4096)  # 4 байта

        if not request:
            break
        else:
            response = f"Hello World\n".encode()
            client_socket.send(response)

    client_socket.close()
