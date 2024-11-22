import socket
import threading

def handle_receive(connection):
    while True:
        data = connection.recv(1024).decode()
        if data:
            print(f"\nPesan dari {connection.getpeername()}: {data}")

def handle_send(connection):
    while True:
        message = input("Anda: ")
        connection.send(message.encode())

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Menunggu koneksi...")
    connection, address = server_socket.accept()
    print(f"Koneksi dari: {address}")

    receive_thread = threading.Thread(target=handle_receive, args=(connection,))
    send_thread = threading.Thread(target=handle_send, args=(connection,))

    receive_thread.start()
    send_thread.start()

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=handle_receive, args=(client_socket,))
    send_thread = threading.Thread(target=handle_send, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

if __name__ == '__main__':
    mode = input("Apakah Anda ingin menjadi server atau client? (server/client): ").strip().lower()
    if mode == 'server':
        server_program()
    elif mode == 'client':
        client_program()
    else:
        print("Mode tidak valid. Pilih 'server' atau 'client'.")