import socket
import threading

# Constants
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Get local machine IP address
ADDR = (SERVER, PORT)

# Initialize server socket (TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Function to handle individual client connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            # Receive the length of the incoming message
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)  # Convert received length to integer
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == DISCONNECT_MESSAGE:
                    connected = False  # Break the loop if disconnect message is received

                print(f"[{addr}] {msg}")  # Print received message from the client
            else:
                connected = False  # If no valid message length, terminate the connection

        except (ValueError, ConnectionResetError, ConnectionAbortedError) as e:
            print(f"[ERROR] {e} from {addr}.")
            connected = False  # Terminate the loop if an error occurs

    conn.close()  # Close the connection
    print(f"[DISCONNECTED] {addr} disconnected.")

# Start listening for client connections
def start():
    server.listen()  # Listen for incoming connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        # Accept incoming connection
        conn, addr = server.accept()
        # Create a new thread for each client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Print active connections (subtract 1 for the main thread)
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] The server is starting...")
start()
