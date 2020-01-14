import socket

HOST = '127.0.0.1'
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            handle_echo(addr, conn)

def handle_echo(addr, conn):
    print('Connected by', addr)

    full_data = conn.recv(BUFFER_SIZE)

    print(f'Received data {full_data} from {addr}')
    conn.sendall(full_data)

    after_send_data = conn.recv(BUFFER_SIZE)
    print(f'After response received data {after_send_data} from {addr}')

    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == '__main__':
    main()