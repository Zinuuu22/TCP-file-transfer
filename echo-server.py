import socket

# Server-side settings
SERVER_HOST = '127.0.0.1'  # Listen on all available interfaces
SERVER_PORT = 5001  # Port to listen on

# Buffer size for file chunks
BUFFER_SIZE = 1024

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    # Accept client connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Open a file to save the received data
    with open("received_file.txt", "wb") as file:
        while True:
            # Receive file chunks
            data = conn.recv(BUFFER_SIZE)
            if not data:  # End of file
                break
            file.write(data)
    
    print("File transfer complete. File saved as 'received_file.txt'")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
