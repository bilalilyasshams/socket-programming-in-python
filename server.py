import socket
import threading


HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == DISCONNECT_MESSAGE:
                    connected = False 

                print(f"[{addr}] {msg}")  
            else:
                connected = False 

        except (ValueError, ConnectionResetError, ConnectionAbortedError) as e:
            print(f"[ERROR] {e} from {addr}.")
            connected = False 

    conn.close()  
    print(f"[DISCONNECTED] {addr} disconnected.")
def start():
    server.listen() 
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] The server is starting...")
start()
