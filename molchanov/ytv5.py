import socket
from select import select

# David Beazley
# 2015 PyCon
# Concurrency from the Ground up Live (Конкурентность в Python с нуля в живую)

tasks = []
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:
        print('accept')
        yield ("read", server_socket)
        client_socket, client_address = server_socket.accept()  # read
        print(f'Connected by: {client_address}')
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        print('recv')
        yield ("read", client_socket)
        request = client_socket.recv(4096)  # read 4 байта

        if not request:
            break
        else:
            response = f"Hello World\n".encode()
            yield ("write", client_socket)
            client_socket.send(response)  # write

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_read, ready_write, _ = select(to_read, to_write, [])

            for sock in ready_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)

            reason, sock = next(task)

            if reason == "read":
                to_read[sock] = task
            if reason == "write":
                to_write[sock] = task
        except StopIteration:
            print("Done")

tasks.append(server())
event_loop()