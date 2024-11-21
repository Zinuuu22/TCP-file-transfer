import socket

# Client-side settings
SERVER_HOST = '127.0.0.1'  # Server IP address
SERVER_PORT = 5001  # Server port
BUFFER_SIZE = 1024  # Buffer size for file chunks

def send_file(file_path):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server {SERVER_HOST}:{SERVER_PORT}")

    # Open the file and send its contents
    with open(file_path, "rb") as file:
        while (chunk := file.read(BUFFER_SIZE)):
            client_socket.sendall(chunk)
    
    print("File transfer complete.")
    client_socket.close()

if __name__ == "__main__":
    file_path = "file_to_send.txt"  # Specify the file to send
    send_file(file_path)
