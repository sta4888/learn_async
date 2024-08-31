import socket
from select import select

# ассинхронность на функциях


# .fileno() - файловый дискриптор это id
# функция select мониторит

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()


def accept_connection(server_socket):
    print('accept')
    client_socket, client_address = server_socket.accept()
    print(f'Connected by: {client_address}')
    to_monitor.append(client_socket)


def send_message(client_socket):
    print('recv')
    request = client_socket.recv(4096)  # 4 байта

    if request:
        response = f"Hello World\n".encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
