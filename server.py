import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Initialize server and client list
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = {}

# Function to handle broadcasting messages to all clients
def broadcast(message, _conn=None):
    for client in clients:
        if client != _conn:  # Avoid sending the message back to the sender
            try:
                client.send(message)
            except BrokenPipeError:
                clients.pop(client)  # Remove the client if sending fails

# Function to handle individual client connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Enter your name: ".encode(FORMAT))
    name = conn.recv(HEADER).decode(FORMAT).strip()
    
    if not name:
        name = f"User{addr[1]}"  # Assign a default name based on port if none provided
    
    welcome_message = f"{name} has joined the chat!".encode(FORMAT)
    broadcast(welcome_message, conn)
    conn.send("Welcome to the chat!".encode(FORMAT))
    
    clients[conn] = name
    connected = True

    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    clients.pop(conn)
                    leave_message = f"{name} has left the chat.".encode(FORMAT)
                    broadcast(leave_message)
                else:
                    print(f"[{name}] {msg}")
                    broadcast(f"[{name}] {msg}".encode(FORMAT), conn)
            else:
                connected = False

        except (ValueError, ConnectionResetError, ConnectionAbortedError) as e:
            print(f"[ERROR] {e} from {addr}.")
            connected = False
            if conn in clients:
                clients.pop(conn)

    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

# Function to start the server and listen for new connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# Start the server
print("[STARTING] The server is starting...")
start()
